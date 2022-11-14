# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from config import get_settings
# import os 

# # retrieve ENV settings from cache
# st = get_settings()

# SQLALCHEMY_DATABASE_URL = f'postgresql://{st.DBUSER}:{st.DBPASS}@{st.DBHOST}:{st.DBPORT}/{st.DBNAME}'

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL,
#     pool_pre_ping=True,
# )

# DatabaseSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()


# def db():
#     database = DatabaseSession()
#     try:
#         yield database
#     finally:
#         database.close()
