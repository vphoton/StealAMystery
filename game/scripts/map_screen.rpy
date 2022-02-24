




screen map_screen(aMap):

    add "#47f641"

    # add map image and center the view to it
    $offset_x = 800 - (128 * aMap.center_x)
    $offset_y = 500 - (128 * aMap.center_y)
    add aMap.img:
        pos(offset_x, offset_y)

    # go through map array and check if occupant is there to place it's image
    for i in range(len(aMap.map)):
        $row = aMap.map[i]
        for j in range(len(row)):
            $tile = row[j]
            if not tile.occupant is None and isinstance(tile.occupant, MapDenizen):
                $offx, offy = tile.occupant.getOffset()
                $tile_lc_x = 128 * j + offset_x
                $tile_lc_y = 128 * i + offset_y
                add tile.occupant.img:
                    pos(tile_lc_x + offx, tile_lc_y + offy)

    # move character around the screen
    # this lets you do multiple things in an action
    #key "K_UP" action [function(main_map.moveDenizen, player_sprite.x, player_sprite.y, 0, -1), SetVariable("k_dir", "back")]
    key "K_UP" action [Function(main_map.moveDenizen, player_sprite.x, player_sprite.y, 0, -1), SetVariable("k_dir", "back")]
    key "K_DOWN" action [Function(main_map.moveDenizen, player_sprite.x, player_sprite.y, 0, 1), SetVariable("k_dir", "front")]
    key "K_LEFT" action [Function(main_map.moveDenizen, player_sprite.x, player_sprite.y, -1, 0), SetVariable("k_dir", "left")]
    key "K_RIGHT" action [Function(main_map.moveDenizen, player_sprite.x, player_sprite.y, 1, 0), SetVariable("k_dir", "right")]
    key "K_RETURN" action Function(playerInteracts)
