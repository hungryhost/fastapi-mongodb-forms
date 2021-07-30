#! /bin/bash

mongoimport --host mongodb --db forms --collection form_collection --type json --file /mongo-seed/forms_collection.json --jsonArray