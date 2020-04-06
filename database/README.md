## Introduction

Database structure is documented with SchemaSpy: http://schemaspy.org/.

This tool generates HTML files with information on schemas, tables, functions, constraints and provide graphical representation of the table relations.

## Documentation SchemaSpy

We created a small bash script to generate the documentation

```bash
chmod +x build_database_documentation.sh
```

Run it by passing correct database connection parameters (password will be asked)

/!\ Temporary edit the schema in the script:

Either : `-s adresse`
Or : `-schemas raepa,audit`

```bash
./build_database_documentation.sh -h localhost -p 5432 -d adresse -u postgres -o ../../../docs
```

Il will create an `index.html` file in the `docs/` folder in the root directory, which can be opened with a web browser

NB: Get needed binaries here, or use the `download_schemaspy.sh`:

* SchemaSpy: https://github.com/schemaspy/schemaspy/releases Par exemple `schemaspy-6.1.0.jar`
* Driver PostgreSQL: https://jdbc.postgresql.org/download.html Par exemple `postgresql-42.2.10.jar`
