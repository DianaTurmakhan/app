from sqlalchemy import create_engine
import pandas as pd
import streamlit as st
import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table, Column
from sqlalchemy.sql import text
import datetime
from sqlalchemy import insert
from sqlalchemy import update
import psycopg2


# first table 
p_engine = create_engine(
        st.secrets['postgres'],
        connect_args={'options': f'-csearch_path=Assignment2'}
    )

metadata = db.MetaData()

discover = db.Table('discover', metadata, autoload=True, autoload_with=p_engine)

def create_table():
   p_engine.execute("CREATE TABLE IF  NOT EXISTS disease_type(id INT PRIMARY KEY, description VARCHAR(140))")

def write_record(id,description,p_engine):
    p_engine.execute("INSERT INTO disease_type (id,description) VALUES ('%i','%s')" % (id,description))
    

def view_all_data():
    result = p_engine.execute("SELECT * FROM disease_type ORDER BY id ASC")
    return result.fetchall()


def  view_all_id():
    result = p_engine.execute("SELECT id FROM disease_type")
    return result.fetchall()

def update_record(new_data,id):
    p_engine.execute("UPDATE disease_type SET description= '%s' WHERE id='%i'" % (new_data,id))

def delete_record(id,description):
    p_engine.execute("DELETE FROM disease_type  WHERE id='%i' AND description='%s'" % (id,description))

def  view_id(description):
    result = p_engine.execute("SELECT id FROM disease_type WHERE description ='%s'" % (description))
    return result.fetchall()

def get_description(id):
    result = p_engine.execute("SELECT DISTINCT description FROM disease_type WHERE id ='%i' LIMIT 1" % (id))
    return result.fetchall()

def view_all_desc():
    result = p_engine.execute("SELECT description FROM disease_type GROUP BY description")
    return result.fetchall()






#second table
def create_table2():
   p_engine.execute("CREATE TABLE IF  NOT EXISTS disease(idisease_code VARCHAR(50) PRIMARY KEY, pathogen VARCHAR(20), description VARCHAR(140), id INT, FOREIGN KEY(id) References DiseaseType(id))")
   
def view_all_data2():
    result = p_engine.execute("SELECT * FROM disease ORDER BY id ASC")
    return result.fetchall()


def write_record2(id,description,pathogen, disease_code,p_engine):
    p_engine.execute("INSERT INTO disease (disease_code,pathogen,description,id) VALUES ('%s','%s','%s','%i')" % (disease_code,pathogen,description,id))

def  view_all_id2():
    result = p_engine.execute("SELECT DISTINCT id FROM disease_type")
    return result.fetchall()

def view_all_disease_code():
    result = p_engine.execute("SELECT disease_code FROM disease")
    return result.fetchall()

def get_row(selected_code):
    result = p_engine.execute("SELECT * FROM disease WHERE disease_code ='%s'" % (selected_code))
    return result.fetchall()

def update_record2(new_code, new_pathogen,new_description,new_id,code):
    p_engine.execute("UPDATE disease SET disease_code='%s', pathogen= '%s', description= '%s', id='%i' WHERE disease_code='%s'" % (new_code,new_pathogen,new_description,new_id,code))

def delete_record(code):
    p_engine.execute("DELETE FROM disease  WHERE disease_code='%s'" % (code))



#third table
def create_table3():
   p_engine.execute("CREATE TABLE IF  NOT EXISTS disease(disease_code VARCHAR(50) PRIMARY KEY, pathogen VARCHAR(20), description VARCHAR(140), id INT, FOREIGN KEY(id) References DiseaseType(id))")
   
def view_all_data3():
    result = p_engine.execute("SELECT * FROM country")
    return result.fetchall()

def write_record3(country,population,p_engine):
    p_engine.execute("INSERT INTO country(cname,population) VALUES ('%s','%i')" % (country,population))


def view_all_countries():
    result = p_engine.execute("SELECT cname FROM country")
    return result.fetchall()

def get_row3(selected_country):
    result = p_engine.execute("SELECT * FROM country WHERE cname ='%s'" % (selected_country))
    return result.fetchall()

def update_record3(selected_country,new_population):
    p_engine.execute("UPDATE country SET population='%i' WHERE cname='%s'" % (new_population,selected_country))

def delete_record3(country):
    p_engine.execute("DELETE FROM country  WHERE cname='%s'" % (country))




#fifth table
def create_table5():
   p_engine.execute("CREATE TABLE  IF NOT EXISTS users(email VARCHAR(60), name VARCHAR(30), surname VARCHAR(40), salary INT, phone VARCHAR(20), cname VARCHAR(50), FOREIGN KEY(cname)References Country (cname))")

def view_all_data5():
    result = p_engine.execute("SELECT * FROM users")
    return result.fetchall()

def write_record5(email,name,surname,salary,phone,new_cname,p_engine):
    p_engine.execute("INSERT INTO users(email,name,surname,salary,phone,cname) VALUES ('%s','%s','%s','%i','%i','%s')" % (email,name,surname,salary,phone,new_cname))


def view_whole_email():
    result = p_engine.execute("SELECT DISTINCT email FROM users")
    return result.fetchall()

def get_row5(email):
    result = p_engine.execute("SELECT * FROM users WHERE email ='%s'" % (email))
    return result.fetchall()

def update_record5(email,name,surname,salary,phone,new_cname):
    p_engine.execute("UPDATE users SET name='%s', surname='%s',salary='%i',phone='%s',cname='%s' WHERE email='%s'" % (name,surname,salary,phone,new_cname,email))

def delete_record5(email):
    p_engine.execute("DELETE FROM users WHERE email='%s'" % (email))


#forth table
def create_table4():
   p_engine.execute("CREATE TABLE IF NOT EXISTS doctor(email VARCHAR(60), degree VARCHAR(20),FOREIGN KEY(email) References Users (email))")

def view_all_data4():
    result = p_engine.execute("SELECT * FROM doctor")
    return result.fetchall()

def write_record4(email,degree,p_engine):
    p_engine.execute("INSERT INTO doctor(email,degree) VALUES ('%s','%s')" % (email,degree))


def view_all_emails():
    result = p_engine.execute("SELECT DISTINCT email FROM doctor")
    return result.fetchall()

def get_row4(email):
    result = p_engine.execute("SELECT * FROM doctor WHERE email ='%s'" % (email))
    return result.fetchall()

def view_doctor_emails():
    result = p_engine.execute("SELECT email FROM doctor")
    return result.fetchall()
   

def update_record4(email,degree):
    p_engine.execute("UPDATE doctor SET degree='%s' WHERE email='%s'" % (degree,email))

def delete_record4(email):
    p_engine.execute("DELETE FROM doctor  WHERE email='%s'" % (email))


#sixth table
def create_table6():
   p_engine.execute("CREATE TABLE IF NOT EXISTS public_servant(email VARCHAR(60), department VARCHAR(50),FOREIGN KEY(email) References Users (email)) ")

def view_all_data6():
    result = p_engine.execute("SELECT * FROM public_servant")
    return result.fetchall()

def write_record6(email,degree,p_engine):
    p_engine.execute("INSERT INTO public_servant(email,department) VALUES ('%s','%s')" % (email,degree))


def view_all_emails():
    result = p_engine.execute("SELECT DISTINCT email FROM public_servant")
    return result.fetchall()

def get_row6(email):
    result = p_engine.execute("SELECT * FROM public_servant WHERE email ='%s'" % (email))
    return result.fetchall()

def update_record6(email,degree):
    p_engine.execute("UPDATE public_servant SET department='%s' WHERE email='%s'" % (degree,email))

def delete_record6(email):
    p_engine.execute("DELETE FROM public_servant  WHERE email='%s'" % (email))



#seventh table
def create_table7():
   p_engine.execute("CREATE TABLE IF NOT EXISTS specialize(id INT, email VARCHAR(60),FOREIGN KEY(id) References DiseaseType(id), FOREIGN KEY (email)REFERENCES Doctor (email))")

def view_all_data7():
    result = p_engine.execute("SELECT * FROM specialize ORDER BY id")
    return result.fetchall()

def write_record7(id,email,p_engine):
    p_engine.execute("INSERT INTO specialize(id,email) VALUES ('%i','%s')" % (id,email))


def get_id7(email):
    result = p_engine.execute("SELECT id FROM specialize WHERE email ='%s'" % (email))
    return result.fetchall()

def view_spec_email():
    result = p_engine.execute("SELECT DISTINCT email FROM specialize")
    return result.fetchall() 


def update_record7(new_id,selected_email,selected_id):
    p_engine.execute("UPDATE specialize SET id='%i' WHERE email='%s'" % (new_id,selected_email))


def delete_record7(selected_email,id):
    p_engine.execute("DELETE FROM specialize  WHERE email='%s' AND id='%i' "  % (selected_email,id))

def view_all_spec_emails():
    result = p_engine.execute("SELECT DISTINCT email FROM specialize")
    return result.fetchall()
    
def get_row7(email):
    result = p_engine.execute("SELECT * FROM specialize WHERE email ='%s'" % (email))
    return result.fetchall()



#8th table
def create_table8():
   p_engine.execute("""CREATE TABLE IF NOT EXISTS record(email VARCHAR(60), cname VARCHAR(50), disease_code VARCHAR(50), total_deaths INT, 
					total_patients INT,
					FOREIGN KEY(disease_code) References Disease (disease_code), 
					FOREIGN KEY(cname) References Country (cname), 
					FOREIGN KEY(email) References PublicServant (email))""")

def view_all_data8():
    result = p_engine.execute("SELECT * FROM record")
    return result.fetchall()

def write_record8(email,cname,disease_code, total_death,total_patients,p_engine):
    p_engine.execute("INSERT INTO record(email,cname,disease_code, total_deaths,total_patients) VALUES ('%s','%s','%s','%i','%i')" % (email,cname,disease_code, total_death,total_patients))


def update_record8(email,cname,disease_code,total_death,total_patients):
    p_engine.execute("UPDATE record SET total_deaths='%i', total_patients='%i' WHERE email='%s' AND cname='%s' AND disease_code='%s'" % (total_death,total_patients,email,cname,disease_code))


def delete_record8(email,cname,disease_code):
    p_engine.execute("DELETE FROM record WHERE email='%s' AND cname='%s' AND disease_code='%s' "  % (email,cname,disease_code))

def view_record_emails():
    result = p_engine.execute("SELECT DISTINCT email FROM record")
    return result.fetchall()

def view_record_cname(selected_email):
    result = p_engine.execute("SELECT DISTINCT cname FROM record WHERE email='%s'" % (selected_email))
    return result.fetchall()

def view_record_code(selected_email,cname):
    result = p_engine.execute("SELECT DISTINCT disease_code FROM record WHERE email='%s' AND cname='%s'" % (selected_email,cname))
    return result.fetchall()

def get_row8(email,cname,disease_code):
    result = p_engine.execute("SELECT * FROM record WHERE email='%s' AND cname='%s' AND disease_code='%s'" % (email,cname,disease_code))
    return result.fetchall()



#9table
def create_table9():
   p_engine.execute("""CREATE TABLE IF NOT EXISTS discover(cname VARCHAR(50), disease_code VARCHAR(50),
					  first_enc_date DATE,
					  FOREIGN KEY(disease_code)References Disease(disease_code), 
					  FOREIGN KEY(cname) REFERENCES Country (cname))""")

def view_all_data9():
    result = p_engine.execute("SELECT * FROM discover")
    return result.fetchall()

def write_record9(cname,disease_code, first_enc_date,p_engine):
     stmt = insert(discover).values(cname=cname, disease_code=disease_code,first_enc_date=first_enc_date)
     p_engine.execute(stmt)

def update_record9(cname,disease_code,first_enc_date):
    stmt = update(discover).where(discover.c.cname==cname).where(discover.c.disease_code==disease_code).values(first_enc_date=first_enc_date) 
    p_engine.execute(stmt)

def delete_record9(cname,disease_code):
    p_engine.execute("DELETE FROM discover WHERE cname='%s' AND disease_code='%s' "  % (cname,disease_code))


def view_discover_cname():
    result = p_engine.execute("SELECT cname FROM discover")
    return result.fetchall()

def view_discover_code(cname):
    result = p_engine.execute("SELECT DISTINCT disease_code FROM discover WHERE cname='%s'" % (cname))
    return result.fetchall()

def get_row9(cname,disease_code):
    result = p_engine.execute("SELECT * FROM discover WHERE  cname='%s' AND disease_code='%s'" % (cname,disease_code))
    return result.fetchall()


