import cx_Freeze

executables = [cx_Freeze.Executable("Catcher.py")]

cx_Freeze.setup(
    name = "Ball Shooter",
    options={"build_exe": {"packages":["idna", "pygame", "sys", "random", "trainer_library", 
                                       "moving_ball", "ralts_library", "dratini_library", 
                                       "drifloon_library", "poocheyana_library", "caterpie_library", 
                                       "rat_library", "pidgey_library", "leaf_library", "sprite_sheet", 
                                       "sprite_sheet2", "sprite_sheet3","pulse_library", 
                                       "crescent_library", "tornado_library", "fire_library", 
                                       "wall_library"], 
                           "include_files": ["poppy.png", "ball_background.png", "victory.jpg",
                                              "death.gif", "ball.gif", "ballG.gif", "Caterpie.gif", 
                                              "pidg.gif", "Rat.gif", "Ralts.gif", "Poocheyana.gif", 
                                              "Dratini.gif", "Drifloon.gif", "Blackout C.gif", 
                                              "Blackout P.gif", "Blackout RT.gif", "Blackout R.gif", 
                                              "Blackout PO.gif", "Blackout DR.gif", "Blackout D.gif", 
                                              "Crescent-sheet.png", "Leaf-sheet.png", "fire-sheet.png", 
                                              "pulse-sheet.png", "sprite sheet 1.png", "ball-sheet.png",
                                              "woosh-sheet.png", "throw.ogg", "ball - catch.ogg", "skip.ogg",
                                              "victory.ogg", "lose.ogg", "game_sound.ogg"]}},
    executables = executables
    

)


