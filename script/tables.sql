CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> c18ea807c434

CREATE TABLE client (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    first_name VARCHAR(60), 
    last_name VARCHAR(60), 
    phone VARCHAR(20), 
    address VARCHAR(120), 
    age SMALLINT, 
    PRIMARY KEY (id)
);

CREATE TABLE component (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    name VARCHAR(120), 
    price FLOAT, 
    amount FLOAT, 
    PRIMARY KEY (id), 
    UNIQUE (name), 
    UNIQUE (name)
);

CREATE TABLE medicine (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    name VARCHAR(120), 
    storage_time DATE, 
    amount FLOAT, 
    price FLOAT, 
    type ENUM('pill','ointment','tincture','mixture','liquor','powder'), 
    PRIMARY KEY (id), 
    UNIQUE (name), 
    UNIQUE (name)
);

CREATE TABLE cooking_book (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    medicine_id INTEGER, 
    method ENUM('mixing','creaming'), 
    PRIMARY KEY (id), 
    FOREIGN KEY(medicine_id) REFERENCES medicine (id) ON DELETE CASCADE
);

CREATE TABLE critical_norm (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    component_id INTEGER, 
    amount FLOAT, 
    PRIMARY KEY (id), 
    FOREIGN KEY(component_id) REFERENCES component (id) ON DELETE CASCADE
);

CREATE TABLE ingredient (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    component_id INTEGER, 
    dose FLOAT, 
    PRIMARY KEY (id), 
    FOREIGN KEY(component_id) REFERENCES component (id) ON DELETE CASCADE
);

CREATE TABLE orders (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    `status` ENUM('in_process','waiting_for_components','ready','closed') NOT NULL, 
    client_id INTEGER, 
    medicine_id INTEGER, 
    date_created DATE NOT NULL,
    ready_time DATE,
    PRIMARY KEY (id), 
    FOREIGN KEY(client_id) REFERENCES client (id) ON DELETE CASCADE,
    FOREIGN KEY(medicine_id) REFERENCES medicine (id) ON DELETE CASCADE
);

CREATE TABLE supply_request (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    component_id INTEGER, 
    client_id INTEGER, 
    PRIMARY KEY (id), 
    FOREIGN KEY(client_id) REFERENCES client (id) ON DELETE CASCADE,
    FOREIGN KEY(component_id) REFERENCES component (id) ON DELETE CASCADE
);

CREATE TABLE ingredient_medicine (
    ingredient_id INTEGER, 
    medicine_id INTEGER, 
    FOREIGN KEY(ingredient_id) REFERENCES ingredient (id) ON DELETE CASCADE,
    FOREIGN KEY(medicine_id) REFERENCES medicine (id) ON DELETE CASCADE
);

CREATE TABLE recipe (
    id INTEGER NOT NULL AUTO_INCREMENT, 
    medicine_name VARCHAR(120), 
    doctor VARCHAR(255), 
    client_id INTEGER, 
    diagnosis VARCHAR(255), 
    amount FLOAT, 
    consumption_type ENUM('internal','external','mixing'),
    order_id INTEGER, 
    PRIMARY KEY (id), 
    FOREIGN KEY(client_id) REFERENCES client (id) ON DELETE CASCADE,
    FOREIGN KEY(order_id) REFERENCES orders (id) ON DELETE CASCADE
);

INSERT INTO alembic_version (version_num) VALUES ('c18ea807c434');

