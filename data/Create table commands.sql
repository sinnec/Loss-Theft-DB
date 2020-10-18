BEGIN TRANSACTION;
CREATE TABLE "entries" (
	`id_number` TEXT NOT NULL,
	`surname` TEXT NOT NULL,
	`name` TEXT NOT NULL,
	`reason` TEXT NOT NULL,
	`office_article` TEXT NOT NULL,
	`office_type` INTEGER NOT NULL,
	`office_name` TEXT NOT NULL,
	`protocol_num` TEXT,
	`protocol_date` TEXT,
	`passport` INTEGER,
	`drivers_licence` INTEGER,
	`timestamp` TEXT,
	PRIMARY KEY(`id_number`)
);
CREATE UNIQUE INDEX `id_index` ON `entries` (`id_number`);
COMMIT;
