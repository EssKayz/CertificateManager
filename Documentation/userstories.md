
# Users
- [x] It is possible to create an user
<details><summary> Click to view SQL </summary>
<p>

```SQL
INSERT INTO account (date_created, date_modified, name, username, password
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)
```

</p></details>

- [x] It is possible to login with a created user

## Equipment
- [x] Users can add equipment by manufacturer and model to their own profile from the list of models
<details><summary> Click to view SQL </summary>
<p>

```SQL
INSERT INTO equipment (date_created, date_modified, model_id, person_id, serialnumber, isbroken) 
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?, ?)
```

</p></details>

- [x] Users can view all their existing equipment 
<details><summary> Click to view SQL </summary>
<p>

```SQL
SELECT equipment.id, equipment.person_id AS equipment_person_id, 
equipment.date_created, equipment.date_modified, equipment.model_id, equipment.serialnumber, equipment.isbroken
FROM equipment
WHERE ? = equipment.person_id
```

</p></details>

- [x] Users can mark one of their equipment as broken, or fixed.
<details><summary> Click to view SQL </summary>
<p>

```SQL
UPDATE equipment SET date_modified=CURRENT_TIMESTAMP, isbroken=? WHERE equipment.id = ?
```

</p></details>

- [x] Users can delete equipment from their own list
<details><summary> Click to view SQL </summary>
<p>

```SQL
DELETE FROM equipment WHERE equipment.id = ?
```

</p></details>

# Manufacturers
- [x] Anyone can view a list of device manufacturers (Samsung, SteelSeries, Apple)
<details><summary>Click to view SQL</summary>
<p>

```SQL
 SELECT * FROM Manufacturer
```
</p></details>

- [x] Anyone can view a list of models/products made by each manufacturer
<details><summary>Click to view SQL</summary>
<p>

```SQL
 SELECT * FROM Product WHERE product.manufacturer_id = ?
```
</p></details>

- [x] Anyone can see the top 5 manufacturers with the most products/models
<details><summary>Click to view SQL</summary>
<p>

```SQL
 SELECT Manufacturer.id, COUNT(Product.name) as count, Manufacturer.name FROM Manufacturer, Product
 WHERE Manufacturer.id = Product.manufacturer_id 
 GROUP BY Manufacturer.id 
 ORDER BY count DESC 
 LIMIT 5
```
</p></details>
	
- [x] Users can add a new device manufacturer to the list (Samsung)
<details><summary>Click to view SQL</summary>
<p>

```SQL
INSERT INTO manufacturer (date_created, date_modified, name) 
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?)
```
</p></details>

# Models
- [x] Anyone can view a top-10 list of the least prone to breaking models
<details><summary>Click to view SQL</summary>
<p>

```SQL
SELECT product.id, 
       product.name, 
       (SELECT 100.0 * (SELECT Count(*) 
                        FROM   equipment 
                        WHERE  equipment.model_id = product.id 
                               AND equipment.isbroken) / (SELECT Count(*) 
                                                          FROM   equipment 
                                                          WHERE equipment.model_id = product.id)) 
		AS brokenavg 
FROM   product 
WHERE  brokenavg IS NOT NULL 
GROUP  BY product.id 
ORDER  BY brokenavg ASC 
LIMIT  10 
```

</p></details>

- [x] Anyone can view all existing models
<details><summary>Click to view SQL</summary>
<p>

```SQL
 SELECT * FROM Product
```
</p></details>

- [x] Users can add a new equipment model for a manufacturer (Galaxy S7, by Samsung)
<details><summary>Click to view SQL</summary>
<p>

```SQL
 INSERT INTO product (date_created, date_modified, name, manufacturer_id, eol) 
 VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?, ?)
```
</p></details>

- [x] Users can mark a model as EOL (Product is no longer manufactured / End Of Life)
<details><summary> Click to view SQL </summary>
<p>

```SQL
UPDATE product SET date_modified=CURRENT_TIMESTAMP, eol=? WHERE product.id = ?
```

</p></details>


# Classifications
- [x] Anyone can view all existing classifications, and see which products are linked to them
- [x] Users can add new classifications with a description
<details><summary> Click to view SQL </summary>
<p>

```SQL
INSERT INTO "Classification" (date_created, date_modified, name, description) 
VALUES (CURRENT_TIMESTAMP, CURRENT_TIMESTAMP, ?, ?)
```

</p></details>

- [x] Users can edit the descriptions of the classifications
<details><summary> Click to view SQL </summary>
<p>

```SQL
UPDATE "Classification" SET date_modified=CURRENT_TIMESTAMP, description=? 
WHERE "Classification".id = ?
```

</p></details>

- [x] Users can delete classifications without deleting linked products
<details><summary> Click to view SQL </summary>
<p>

```SQL
DELETE FROM "ClassificationProduct" 
       WHERE "ClassificationProduct".classification_id = ? 
              AND "ClassificationProduct".product_id = ?
DELETE FROM "Classification" 
       WHERE "Classification".id = ?
```

</p></details>

- [x] Users can add classifications to products (Samsung Galaxy S7 has the classification rating "IP68")
<details><summary> Click to view SQL </summary>
<p>

```SQL
INSERT INTO "ClassificationProduct" (classification_id, product_id) VALUES (?, ?)
```

</p></details>

## Stuff that will be implemented post-course / is not relevant for intents of the course

- [ ] Users can add certificates to their own equipment.
- [ ] Users can set certificate lifespan (How long certificate is valid)
- [ ] Users can view their certificates on one list, and sort them by next-to-expire
- [ ] Users can add optional calibration coefficients to their equipment
- [ ] Users can add warranty information to equipment
- [ ] Users can add a copy of their receipt to the warranty information


<style>
       p, ul {
              margin-bottom: 0px !important;
       }
       summary {
              margin-left: 2rem;
              opacity: 0.85;
              font-style: italic;
       }
       summary::-webkit-details-marker {
              opacity: 0.85;
       }

</style>