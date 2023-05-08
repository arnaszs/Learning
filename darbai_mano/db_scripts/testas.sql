CREATE TABLE mokytojai (
  id INT PRIMARY KEY,
  vardas VARCHAR(255) NOT NULL,
  pavarde VARCHAR(255) NOT NULL,
  specialybe VARCHAR(255) NOT NULL,
  nuo_kada_dirba_metais INT
);

INSERT INTO mokytojai (id, vardas, pavarde, specialybe, nuo_kada_dirba_metais)
VALUES(1, 'Petras', 'Petraitis', 'Matematika', '2013'),
    (2, 'Ona', 'Onaitė', 'Fizika', '2012'),
    (3, 'Marius', 'Marijus', 'Biologija', '2015'),
    (4, 'Rasa', 'Rasaitė', 'Anglų', '2011'),
    (5, 'Aurimas', 'Aurimaitis', 'Lietuvių', '2018'),
    (6, 'Gintare', 'Gintarėlė', 'Istorija', '2020');

SELECT * FROM mokytojai WHERE specialybe = 'Matematika';

SELECT vardas, pavarde, specialybe FROM mokytojai
WHERE (2023 - nuo_kada_dirba_metais) > 8 or (2023 - nuo_kada_dirba_metais) > 9;
    
UPDATE mokytojai
SET pavarde = 'Žolienė'
WHERE vardas = 'Rasa' AND pavarde = 'Rasaitė';

DELETE FROM mokytojai WHERE ID = 4;
