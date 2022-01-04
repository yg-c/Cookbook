CREATE TABLE category(
                         id int NOT NULL,
                         name varchar(255),
                         PRIMARY KEY (id)
);

CREATE TABLE course(
                       id int NOT NULL,
                       name varchar(255),
                       PRIMARY KEY (id)
);

CREATE TABLE recipe(
                       id int NOT NULL,
                       name varchar(255),
                       category_id int NOT NULL,
                       course_id int NOT NULL,
                       pax int,
                       preparation_time int,
                       instructions text,
                       PRIMARY KEY (id),
                       FOREIGN KEY (category_id) REFERENCES category(id),
                       FOREIGN KEY (course_id) REFERENCES course(id)
);

CREATE TABLE ingredient(
                           id int NOT NULL,
                           name varchar(255),
                           PRIMARY KEY (id)
);

CREATE TABLE measurement_unit(
                               id int NOT NULL,
                               name varchar(255),
                               PRIMARY KEY (id)
);

CREATE TABLE ingredient_recipe(
                                 id int NOT NULL,
                                 recipe_id int NOT NULL,
                                 ingredient_id int NOT NULL,
                                 quantity float(10,4),
                                 measurement_unit_id int not NULL,
                                 PRIMARY KEY (id),
                                 FOREIGN KEY (recipe_id) REFERENCES recipe(id),
                                 FOREIGN KEY (ingredient_id) REFERENCES ingredient(id),
                                 FOREIGN KEY (measurement_unit_id) REFERENCES measurement_unit(id)
);