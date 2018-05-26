# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw


class Pydenticon5(object):

    sprites = [
        [(0.5, 1), (1, 0), (1, 1)],  # triangle
        [(0.5, 0), (1, 0), (0.5, 1), (0, 1)],  # parallelogram
        [(0.5, 0), (1, 0), (1, 1), (0.5, 1), (1, 0.5)],  # mouse ears
        [(0, 0.5), (0.5, 0), (1, 0.5), (0.5, 1), (0.5, 0.5)],  # ribbon
        [(0, 0.5), (1, 0), (1, 1), (0, 1), (1, 0.5)],  # sails
        [(1, 0), (1, 1), (0.5, 1), (1, 0.5), (0.5, 0.5)],  # fins
        [(0, 0), (1, 0), (1, 0.5), (0, 0), (0.5, 1), (0, 1)],  # beak
        [(0, 0), (0.5, 0), (1, 0.5), (0.5, 1), (0, 1), (0.5, 0.5)],  # chevron
        [(0.5, 0), (0.5, 0.5), (1, 0.5), (1, 1), (0.5, 1), (0.5, 0.5), (0, 0.5)],  # fish
        [(0, 0), (1, 0), (0.5, 0.5), (1, 0.5), (0.5, 1), (0.5, 0.5), (0, 1)],  # kite
        [(0, 0.5), (0.5, 1), (1, 0.5), (0.5, 0), (1, 0), (1, 1), (0, 1)],  # trough
        [(0.5, 0), (1, 0), (1, 1), (0.5, 1), (1, 0.75), (0.5, 0.5), (1, 0.25)],  # rays
        [(0, 0.5), (0.5, 0), (0.5, 0.5), (1, 0), (1, 0.5), (0.5, 1), (0.5, 0.5), (0, 1)],  # double rhombus
        [(0, 0), (1, 0), (1, 1), (0, 1), (1, 0.5), (0.5, 0.25), (0.5, 0.75), (0, 0.59), (0.5, 0.25)],  # crown
        [(0, 0.5), (0.5, 0.5), (0.5, 0), (1, 0), (0.5, 0.5), (1, 0.5), (0.5, 1), (0.5, 0.5), (0, 1)]  # radioactive
    ]
    default_sprite = [ (0, 0), (1, 0), (0.5, 0.5), (0.5, 0), (0, 0.5), (1, 0.5), (0.5, 1), (0.5, 0.5), (0, 1)] # tiles

    center_sprites = [
        [],  # empty
        [0, 0, 1, 0, 1, 1, 0, 1],  # fill
        [0.5, 0, 1, 0.5, 0.5, 1, 0, 0.5],  # diamond
        [0, 0, 1, 0, 1, 1, 0, 1, 0, 0.5, 0.5, 1, 1, 0.5, 0.5, 0, 0, 0.5],  # reverse diamond
        [0.25, 0, 0.75, 0, 0.5, 0.5, 1, 0.25, 1, 0.75, 0.5, 0.5, 0.75, 1, 0.25, 1, 0.5, 0.5, 0, 0.75, 0, 0.25, 0.5, 0.5],  # cross
        [0, 0, 0.5, 0.25, 1, 0, 0.75, 0.5, 1, 1, 0.5, 0.75, 0, 1, 0.25, 0.5],  # morning star
        [0.33, 0.33, 0.67, 0.33, 0.67, 0.67, 0.33, 0.67],  # small square
        [0, 0, 0.33, 0, 0.33, 0.33, 0.66, 0.33, 0.67, 0, 1, 0, 1, 0.33, 0.67, 0.33, 0.67, 0.67,
          1, 0.67, 1, 1, 0.67, 1, 0.67, 0.67, 0.33, 0.67, 0.33, 1, 0, 1, 0, 0.67, 0.33, 0.67,
          0.33, 0.33, 0, 0.33]  # checkerboard
    ]

    default_center_sprite = [ 0, 0, 1, 0, 0.5, 0.5, 0.5, 0, 0, 0.5, 1, 0.5, 0.5, 1, 0.5, 0.5, 0, 1]  # tiles

    def __init__(self, background=0):
        self.background_color = background

    def _get_sprite(self, shape, size):

        coords = list(self.sprites[shape] if shape < len(self.sprites) else self.default_sprite)

        # scale up
        for i in range(len(coords)):
            coords[i] = (coords[i][0] * size, coords[i][1] * size)

        return coords

    def _get_center_sprite(self, shape, size):
        coords = list(self.center_sprites[shape] if shape < len(self.center_sprites) else self.default_center_sprite)

        # apply ratios
        for i in range(len(coords)):
            coords[i] = coords[i] * size

        return coords

    def draw_rotated_polygon(self, orig, box_size, sprite, x, y, shapeangle, angle, size, fillstyle):

        poly_img = Image.new('RGBA', (box_size, box_size), color=self.background_color)
        ImageDraw.Draw(poly_img).polygon(sprite, fill=fillstyle)

        # .rotate on the 2d canvas in identicon5.js rotates clockwise while pillow rotates counter clockwise
        pillow_angle = -360 - angle
        poly_img = poly_img.rotate(pillow_angle)

        pillow_angle = -360 - shapeangle
        poly_img = poly_img.rotate(pillow_angle)

        orig.paste(poly_img, (x, y))
        
        return orig

    def draw(self, hash, size, rotate=True):

        img = Image.new('RGBA', (size, size), color=self.background_color)

        corner_sprite_shape = int(hash[0], 16)
        side_sprite_shape = int(hash[1], 16)
        center_sprite_shape = int(hash[2], 16) & 7

        center_sprite_background = int(hash[5], 16) % 2

        corner_sprite_rotation = (int(hash[3], 16) & 3) * 90
        side_sprite_rotation = (int(hash[4], 16) & 3) * 90

        # corner sprite foreground color
        cfr = int(hash[6:8], 16)
        cfg = int(hash[8:10], 16)
        cfb = int(hash[10:12], 16)

        # side sprite foreground color
        sfr = int(hash[12:14], 16)
        sfg = int(hash[14:16], 16)
        sfb = int(hash[16:18], 16)

        # size of each sprite
        block_size = int(size / 3)

        # generate corner sprites
        if not rotate:
            corner_sprite_rotation = 0

        corner_sprite = self._get_sprite(corner_sprite_shape, block_size)
        fillstyle = (cfr, cfg, cfb)

        # corner sprites
        # top left
        img = self.draw_rotated_polygon(img, block_size, corner_sprite, 0, 0, corner_sprite_rotation, 0, block_size, fillstyle)
        # top right
        img = self.draw_rotated_polygon(img, block_size, corner_sprite, size - block_size, 0, corner_sprite_rotation, 90, block_size, fillstyle)
        # bottom right
        img = self.draw_rotated_polygon(img, block_size, corner_sprite, size - block_size, size - block_size, corner_sprite_rotation, 180, block_size, fillstyle)
        # bottom left
        img = self.draw_rotated_polygon(img, block_size, corner_sprite, 0, size - block_size, corner_sprite_rotation, 270, block_size, fillstyle)

        # draw sides
        if not rotate:
            side_sprite_rotation = 0

        # side sprites
        side_sprite = self._get_sprite(side_sprite_shape, block_size)
        fillstyle = (sfr, sfg, sfb)

        # left
        img = self.draw_rotated_polygon(img, block_size, side_sprite, 0, block_size, side_sprite_rotation, 0, block_size, fillstyle)
        # top
        img = self.draw_rotated_polygon(img, block_size, side_sprite, 1 * block_size, 0 * block_size, side_sprite_rotation, 90, block_size, fillstyle)
        # right
        img = self.draw_rotated_polygon(img, block_size, side_sprite, 2 * block_size, 1 * block_size, side_sprite_rotation, 180, block_size, fillstyle)
        # bottom
        img = self.draw_rotated_polygon(img, block_size, side_sprite, 1 * block_size, 2 * block_size, side_sprite_rotation, 270, block_size, fillstyle)
        
        # center
        center_sprite = self._get_center_sprite(center_sprite_shape, block_size)

        # make sure there's enough contrast before we use background color of side sprite
        if center_sprite_background > 0 and (abs(cfr - sfr) > 127 or abs(cfg - sfg) > 127 or abs(cfb - sfb) > 127):
            fillstyle = (sfr, sfg, sfb)
        else:
            fillstyle = (cfr, cfg, cfb)

        if center_sprite:
            self.draw_rotated_polygon(img, block_size, center_sprite, block_size, block_size, 0, 0, block_size, fillstyle)
        
        return img
