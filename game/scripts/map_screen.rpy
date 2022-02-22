




screen map_screen(aMap):

    add "#000"

    $offset_x = 640 - (80 * aMap.center_x) + 40
    $offset_y = 280 - (80 * aMap.center_y) + 40
    add aMap.img:
        pos(offset_x, offset_y)

    for i in range(len(aMap.map)):
        $row = aMap.map[i]
        for j in range(len(row)):
            $tile = row[j]
            if not tile.occupant is None and isinstance(tile.occupant, MapDenizen):
                $offx, offy = tile.occupant.getOffset()
                $tile_lc_x = 80 * j + offset_x
                $tile_lc_y = 80 * i + offset_y
                add tile.occupant.img:
                    pos(tile_lc_x + offx, tile_lc_y + offy)

    # this lets you do multiple things in an action
    #key "K_UP" action [function(kotachis_house.moveDenizen, kotachi_sprite.x, kotachi_sprite.y, 0, -1), SetVariable("k_dir", "back")]
    key "K_UP" action function(kotachis_house.moveDenizen, kotachi_sprite.x, kotachi_sprite.y, 0, -1)
    key "K_DOWN" action function(kotachis_house.moveDenizen, kotachi_sprite.x, kotachi_sprite.y, 0, 1)
    key "K_LEFT" action function(kotachis_house.moveDenizen, kotachi_sprite.x, kotachi_sprite.y, -1, 0)
    key "K_RIGHT" action function(kotachis_house.moveDenizen, kotachi_sprite.x, kotachi_sprite.y, 1, 0)
