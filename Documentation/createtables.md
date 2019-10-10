## Manufacturer :
```
CREATE TABLE manufacturer (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144) NOT NULL,
        PRIMARY KEY (id)
)
```

## Classification
```
CREATE TABLE "Classification" (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144) NOT NULL,
        description VARCHAR(144) NOT NULL,
        PRIMARY KEY (id)
)
```

## User / Account
```
CREATE TABLE account (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144) NOT NULL,
        username VARCHAR(144) NOT NULL,
        password VARCHAR(144) NOT NULL,
        PRIMARY KEY (id)
)
```

## Product / Model
```
CREATE TABLE product (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144) NOT NULL,
        manufacturer_id INTEGER NOT NULL,
        eol BOOLEAN NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(manufacturer_id) REFERENCES manufacturer (id),
        CHECK (eol IN (0, 1))
)

```

## ClassificationProduct (junction table between classifications and products)
```
CREATE TABLE "ClassificationProduct" (
        classification_id INTEGER,
        product_id INTEGER,
        FOREIGN KEY(classification_id) REFERENCES "Classification" (id),
        FOREIGN KEY(product_id) REFERENCES product (id)
)
```

## Equipment
```
CREATE TABLE equipment (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        model_id INTEGER NOT NULL,
        person_id INTEGER NOT NULL,
        serialnumber VARCHAR(134),
        isbroken BOOLEAN NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(model_id) REFERENCES product (id),
        FOREIGN KEY(person_id) REFERENCES account (id),
        CHECK (isbroken IN (0, 1))
)
```