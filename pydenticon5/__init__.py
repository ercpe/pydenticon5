# -*- coding: utf-8 -*-
import math

from PIL import Image, ImageDraw


class Pydenticon5(object):

    def _get_sprite(self, shape, size):

        if shape == 0:  # triangle
            coords = [ (0.5, 1), (1, 0), (1, 1) ]
        elif shape == 1:  # parallelogram
            coords = [ (0.5, 0), (1, 0), (0.5, 1), (0, 1) ]
        elif shape == 2:  # mouse ears
            coords = [ (0.5, 0), (1, 0), (1, 1), (0.5, 1), (1, 0.5) ]
        elif shape == 3: # ribbon
            coords = [ (0, 0.5), (0.5, 0), (1, 0.5), (0.5, 1), (0.5, 0.5)]
        elif shape == 4: # sails
            coords = [ (0, 0.5), (1, 0), (1, 1), (0, 1), (1, 0.5)]
        elif shape == 5: # fins
            coords = [ (1, 0), (1, 1), (0.5, 1), (1, 0.5), (0.5, 0.5)]
        elif shape == 6: # beak
            coords = [ (0, 0), (1, 0), (1, 0.5), (0, 0), (0.5, 1), (0, 1)]
        elif shape == 7: # chevron
            coords = [ (0, 0), (0.5, 0), (1, 0.5), (0.5, 1), (0, 1), (0.5, 0.5)]
        elif shape == 8: # fish
            coords = [ (0.5, 0), (0.5, 0.5), (1, 0.5), (1, 1), (0.5, 1), (0.5, 0.5), (0, 0.5)]
        elif shape == 9: # kite
            coords = [ (0, 0), (1, 0), (0.5, 0.5), (1, 0.5), (0.5, 1), (0.5, 0.5), (0, 1)]
        elif shape == 10: # trough
            coords = [ (0, 0.5), (0.5, 1), (1, 0.5), (0.5, 0), (1, 0), (1, 1), (0, 1)]
        elif shape == 11: # rays
            coords = [ (0.5, 0), (1, 0), (1, 1), (0.5, 1), (1, 0.75), (0.5, 0.5), (1, 0.25)]
        elif shape == 12: # double rhombus
            coords = [ (0, 0.5), (0.5, 0), (0.5, 0.5), (1, 0), (1, 0.5), (0.5, 1), (0.5, 0.5), (0, 1)]
        elif shape == 13: # crown
            coords = [ (0, 0), (1, 0), (1, 1), (0, 1), (1, 0.5), (0.5, 0.25), (0.5, 0.75), (0, 0.59), (0.5, 0.25)]
        elif shape == 14: # radioactive
            coords = [ (0, 0.5), (0.5, 0.5), (0.5, 0), (1, 0), (0.5, 0.5), (1, 0.5), (0.5, 1), (0.5, 0.5), (0, 1)]
        else: # tiles
            coords = [ (0, 0), (1, 0), (0.5, 0.5), (0.5, 0), (0, 0.5), (1, 0.5), (0.5, 1), (0.5, 0.5), (0, 1)]

        # scale up

        for i in range(len(coords)):
            coords[i] = (coords[i][0] * size, coords[i][1] * size)

        return coords

    def draw_rotated_polygon(self, orig, box_size, sprite, x, y, shapeangle, angle, size, fillstyle):

        print("Draw rotated polygon: sprite=%s, x=%s, y=%s, shapeangle=%s, angle=%s, size=%s, fillstyle=%s" % (sprite, x, y, shapeangle, angle, size, fillstyle))

        poly_img = Image.new('RGBA', (box_size, box_size))

        # ImageDraw.Draw(poly_img).polygon([
        #     (0, size),
        #     (size/2, 0),
        #     (size, size)
        # ], fill=(255,255,255))
        
        ImageDraw.Draw(poly_img).polygon(sprite, fill=fillstyle)
        
        pillow_angle = (angle - 180) * -1
        poly_img = poly_img.rotate(pillow_angle)
        orig.paste(poly_img, (x, y))
        
        #
        # #img.rotate(angle * math.pi / 180, center=(x, y))
        # if angle == 90:
        #     img = orig.rotate(angle * -1, center=(x, y)) # Pillow rotate is counter clockwise!
        #     img.show()
        # else:
        #     img = orig
        #
        # draw = ImageDraw.Draw(img)
        # draw.rectangle(
        #     [x, y, x+size, y+size], outline=(0,0,0)
        # )
        #
        # #center = (x, y)
        # #img.rotate(angle * math.pi / 180, center=center)
        # #img.rotate(shapeangle, center=(size/2, size/2))
        #
        # # move sprite to the correct box
        # translated_sprite = [
        #     (s[0] + x, s[1] + y) for s in sprite
        # ]
        # draw.polygon(translated_sprite, fill=fillstyle)
        #
        #
        #
        #
        #
        # # # var halfSize = size / 2;
        # # half_size = size / 2
        # #
        # # # # ctx.translate(x, y);
        # # # # ctx.rotate(angle * Math.PI / 180);
        # # center = (x, y)
        # # img.rotate(angle * math.pi / 180, center=center)
        # # #
        # # # # ctx.translate(halfSize, halfSize);
        # # # # ctx.rotate(shapeangle);
        # # center = (half_size, half_size)
        # # img.rotate(shapeangle, center=center)
        # # #
        # # # # var tmpSprite = [];
        # # # # for (var p = 0; p < sprite.length; p++) {
        # # # #     tmpSprite[p] = sprite[p] - halfSize;
        # # # # }
        # # # # fillPoly(ctx, tmpSprite);
        # # tmpsprite = [(coords[0] + center[0] - half_size, coords[1] + center[1] - half_size) for coords in sprite]
        # # draw.polygon(tmpsprite, fillstyle)
        #
        # # debug
        #
        # # img.rotate(shapeangle * -1, center=center)
        # # img.rotate((angle * math.pi / 180) * -1, center=(x, y))
        return orig


    def get_center(self, shape, size):

        if shape == 0:  # empty
            center = []
        elif shape == 1:  # fill
            center = [0, 0, 1, 0, 1, 1, 0, 1]
        elif shape == 2:  # diamond
            center = [ 0.5, 0, 1, 0.5, 0.5, 1, 0, 0.5]

        elif shape == 3:  # reverse diamond
            center = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0.5, 0.5, 1, 1, 0.5, 0.5, 0, 0, 0.5]

        elif shape == 4:  # cross
            center = [ 0.25, 0, 0.75, 0, 0.5, 0.5, 1, 0.25, 1, 0.75, 0.5, 0.5, 0.75, 1, 0.25, 1, 0.5, 0.5, 0, 0.75, 0, 0.25, 0.5, 0.5]

        elif shape == 5:  # morning star
            center = [ 0, 0, 0.5, 0.25, 1, 0, 0.75, 0.5, 1, 1, 0.5, 0.75, 0, 1, 0.25, 0.5]

        elif shape == 6:  # small square
            center = [ 0.33, 0.33, 0.67, 0.33, 0.67, 0.67, 0.33, 0.67]

        elif shape == 7:  # checkerboard
            center = [ 0, 0, 0.33, 0, 0.33, 0.33, 0.66, 0.33, 0.67, 0, 1, 0, 1, 0.33, 0.67, 0.33, 0.67, 0.67,
                    1, 0.67, 1, 1, 0.67, 1, 0.67, 0.67, 0.33, 0.67, 0.33, 1, 0, 1, 0, 0.67, 0.33, 0.67,
                    0.33, 0.33, 0, 0.33]
        else: # tiles
            center = [ 0, 0, 1, 0, 0.5, 0.5, 0.5, 0, 0, 0.5, 1, 0.5, 0.5, 1, 0.5, 0.5, 0, 1]

        # apply ratios
        for i in range(len(center)):
            center[i] = center[i] * size

        return center

    def draw(self, hash, size, rotate):

        img = Image.new('RGBA', (size, size))
        #img = ImageDraw.Draw(i)

        corner_sprite_shape = int(hash[0], 16)
        side_sprite_shape = int(hash[1], 16)
        center_sprite_shape = int(hash[2], 16) & 7

        half_pi = math.pi / 2

        corner_sprite_rotation = half_pi * (int(hash[3], 16) & 3)
        side_sprite_rotation = half_pi * (int(hash[4], 16) & 3)
        center_sprite_background = int(hash[5], 16) % 2

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
        # totalsize = size

        # start with blank 3x3 identicon

        # generate corner sprites
        corner = self._get_sprite(corner_sprite_shape, block_size)
        ### ctx.fillStyle = "rgb(" + cfr + "," + cfg + "," + cfb + ")";

        if not rotate:
            corner_sprite_rotation = 0

        fillstyle = (cfr, cfg, cfb)

        img = self.draw_rotated_polygon(img, block_size, corner, 0, 0, corner_sprite_rotation, 0, block_size, fillstyle)
        img = self.draw_rotated_polygon(img, block_size, corner, size - block_size, 0, corner_sprite_rotation, 90, block_size, fillstyle)
        img = self.draw_rotated_polygon(img, block_size, corner, size - block_size, size - block_size, corner_sprite_rotation, 180, block_size, fillstyle)
        img = self.draw_rotated_polygon(img, block_size, corner, 0, size - block_size, corner_sprite_rotation, 270, block_size, fillstyle)

        # draw sides
        if not rotate:
            side_sprite_rotation = 0

        side = self._get_sprite(side_sprite_shape, size)

        fillstyle = (sfr, sfg, sfb)
        img = self.draw_rotated_polygon(img, block_size, side, 0, block_size, side_sprite_rotation, 0, block_size, fillstyle)
        img = self.draw_rotated_polygon(img, block_size, side, 2 * block_size, 0, side_sprite_rotation, 90, block_size, fillstyle)
        img = self.draw_rotated_polygon(img, block_size, side, 3 * block_size, 2 * block_size, side_sprite_rotation, 180, block_size, fillstyle)
        img = self.draw_rotated_polygon(img, block_size, side, block_size, 3 * block_size, side_sprite_rotation, 270, block_size, fillstyle)
        #
        # center = self.get_center(center_sprite_shape, size)
        #
        # # make sure there's enough contrast before we use background color of side sprite
        #
        # if center_sprite_background > 0 and (abs(cfr - sfr) > 127 or abs(cfg - sfg) > 127 or abs(cfb - sfb) > 127):
        #     fillstyle = (sfr, sfg, sfb)
        # else:
        #     fillstyle = (cfr, cfg, cfb)
        #
        # if center:
        #     self.draw_rotated_polygon(img, center, size, size, 0, 0, size, fillstyle)
        
        return img
