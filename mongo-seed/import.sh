#! /bin/bash

mongoimport --host db --db forms --collection form_collection --type json --file /mongo-seed/forms_collection.json --jsonArray