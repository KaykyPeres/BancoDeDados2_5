from database import Database
from personModel import personModel

db = Database(database="relatorio_5", collection="Livros")
personModel = personModel(database=db)

# 1- Create
#personModel.create_person(1, "Senhor dos aneis A sociedade do anel", "J.R.R TOLKIEN",1954, 29.99)

# 2- Read
#personModel.read_person_by_id("1")

# 3- Update
#personModel.update_person(1, "O Hobbit", "J.R.R TOLKIEN",1956, 19.99)

# 4- Delete
#personModel.delete_person(1)