# TURNCATE
query_foreign_key_check_0 = "SET FOREIGN_KEY_CHECKS=0;"
query_turncate_category = "TRUNCATE TABLE category;"
query_turncate_course = "TRUNCATE TABLE course;"
query_turncate_ingredient = "TRUNCATE TABLE ingredient;"
query_turncate_measurement_unit = "TRUNCATE TABLE measurement_unit;"
query_turncate_recipe = "TRUNCATE TABLE recipe;"
query_turncate_ingredient_recipe = "TRUNCATE TABLE ingredient_recipe;"
query_foreign_key_check_1 = "SET FOREIGN_KEY_CHECKS=1;"

# INSERT
query_populate_category = "INSERT INTO category (id, name)\
                             VALUES  (1, 'Libre'),\
                                     (2, 'Viande'),\
                                     (3, 'Végétarien')\
                             ;"

query_populate_course = "INSERT INTO course (id, name)\
                            VALUES  (1, 'Plat'),\
                                    (2, 'Entrées'),\
                                    (3, 'Dessert')\
                            ;"

query_populate_ingredient = "INSERT INTO ingredient (id, name)\
                                VALUES  (1, 'Oeuf'),\
                                        (2, 'Eau'),\
                                        (3, 'Lait'),\
                                        (4, 'Farine'),\
                                        (5, 'Sel'),\
                                        (6, 'Sucre'),\
                                        (7, 'Huile'),\
                                        (8, 'Émincé de boeuf'),\
                                        (9, 'Fécule de maïs'),\
                                        (10, 'Ail'),\
                                        (11, 'Poivron rouge'),\
                                        (12, 'Oignon'),\
                                        (13, 'Sauce soja'),\
                                        (14, 'Sauce huite'),\
                                        (15, 'Sauce poisson'),\
                                        (16, 'Huile de sésame'),\
                                        (17, 'Basilic thaï')\
                                ;"

query_populate_unit = "INSERT INTO measurement_unit (id, name)\
                        VALUES  (1, 'Pièce'),\
                                (2, 'Décilitre'),\
                                (3, 'Gramme'),\
                                (4, 'CS'),\
                                (5, 'Pointe'),\
                                (6, 'CC'),\
                                (7, 'Gousse'),\
                                (8, 'Paquet')\
                        ;"

query_populate_recipe = "INSERT INTO recipe (id, name, category_id, course_id, pax, preparation_time, instructions)\
                            VALUES(1, 'Crêpes', 1, 1,3, 150, 'Mélanger le tout au robot ménager afin d''éviter les grumeaux.'\
                                 '\n Laisser reposer 2 heures.'),\
                              (2, 'Boeuf Basilic Thaï', 2, 1, 2, 40, 'Dans un grand bol, mettre le boeuf avec la maïzena et 1 c. à soupe d’huile. Bien mélanger.'\
                                 '\n Chauffer le wok à feu vif et ajouter 2 c. à soupe d''huile. Faire sauter le boeuf afin que la viande soit mi-cuite.'\
                                 '\n Ajouter l''ail et l''oignon. Mélanger rapidement et faire cuire à feu vif pendant 30 secondes.'\
                                 '\n Ajouter le poivron rouge et faire sauter environ 1 min.'\
                                 '\n Ajouter la sauce de soja, la sauce aux huîtres, la sauce poisson et le sucre. Faire sauter quelques secondes.')\
                            ;"

query_populate_ingredient_recipe = "INSERT INTO ingredient_recipe(id, recipe_id, ingredient_id, quantity, measurement_unit_id)\
                                        VALUES  (1, 1, 1, 3, 1),\
                                                (2, 1, 2, 1.5, 2),\
                                                (3, 1, 3, 1.5, 2),\
                                                (4, 1, 4, 100, 3),\
                                                (5, 1, 5, 1, 5),\
                                                (6, 1, 6, 1.5, 4),\
                                                (8, 2, 8, 300, 3),\
                                                (9, 2, 9, 2, 6),\
                                                (10, 2, 10, 4, 7),\
                                                (11, 2, 11, 1, 1),\
                                                (12, 2, 12, 1, 1),\
                                                (13, 2, 13, 3, 4),\
                                                (14, 2, 14, 1.5, 4),\
                                                (15, 2, 15, 1, 4),\
                                                (16, 2, 6, 1, 6),\
                                                (17, 2, 16, 2, 4),\
                                                (18, 2, 17, 0.5, 8)\
                                        ;"
