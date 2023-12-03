CREATE TABLE `request` (
  `id_request` int PRIMARY KEY,
  `fk_id_institucion` int,
  `status` enum('active', 'invactive', 'error'),
  `id_proceso` int,
  `nombre` varchar(255),
  `fk_id_ws_samai` int,
  `fk_id_ws_judicial` int,
  `fk_id_location` int,
  `update` datetime,
  `added_at` datetime,
  `modified_at` datetime
);

CREATE TABLE `ws_samai` (
  `id_ws_samai` int PRIMARY KEY,
  `status` enum('update', 'outdated', 'error', 'inactive'),
  `update` datetime,
  `added_at` datetime,
  `modified_at` datetime
);

CREATE TABLE `ws_judicial` (
  `id_ws_judicial` int PRIMARY KEY,
  `status` enum('update', 'outdated', 'error', 'inactive'),
  `update` datetime,
  `added_at` datetime,
  `modified_at` datetime
);

CREATE TABLE `institution` (
  `id_institution` int PRIMARY KEY,
  `name` varchar(255),
  `status` enum('active', 'inactive', 'lock'),
  id_samui int
  id_institution int
  `fk_id_location` int
);

CREATE TABLE `location` (
  `id_location` int PRIMARY KEY,
  `name` varchar(255),
  `type` enum('country', 'department', 'region', 'city'),
  `fk_id_location` int,
  `added_at` datetime,
  `modified_at` datetime
);

CREATE TABLE `actions` (
  `id_action` int PRIMARY KEY,
  `fk_id_request` int,
  `id_filed` varchar(100),
  `detail` text,
  `action` text
);

CREATE TABLE `email` (
  `id_email` int PRIMARY KEY,
  `fk_id_request` int,
  `status` enum('verified', 'not verified'),
  `added_at` datetime
);

ALTER TABLE `actions` ADD FOREIGN KEY (`fk_id_request`) REFERENCES `request` (`id_request`);

ALTER TABLE `request` ADD FOREIGN KEY (`fk_id_institucion`) REFERENCES `institution` (`id_institution`);

ALTER TABLE `ws_samai` ADD FOREIGN KEY (`id_ws_samai`) REFERENCES `request` (`fk_id_ws_samai`);

ALTER TABLE `ws_judicial` ADD FOREIGN KEY (`id_ws_judicial`) REFERENCES `request` (`fk_id_ws_judicial`);

ALTER TABLE `request` ADD FOREIGN KEY (`fk_id_location`) REFERENCES `location` (`id_location`);

ALTER TABLE `location` ADD FOREIGN KEY (`fk_id_location`) REFERENCES `location` (`id_location`);

ALTER TABLE `email` ADD FOREIGN KEY (`fk_id_request`) REFERENCES `request` (`id_request`);
