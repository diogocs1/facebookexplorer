from utils import Utils

import profile
import feed

db = Utils.banco
db.generate_mapping(create_tables=True)