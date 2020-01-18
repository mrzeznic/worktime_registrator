
-- tasks table
CREATE TABLE IF NOT EXISTS tasks (
    id integer PRIMARY KEY AUTOINCREMENT,
    name text NOT NULL,
    project_id integer NOT NULL,
    begin_date date NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects (id)
);
