import pandas as pd
import streamlit as st
import db
import psycopg2


from db import (create_table, delete_record, get_description, p_engine,
                update_record, view_all_data, view_all_desc, view_all_id,
                view_id, write_record)


def main():
    menu = ["disease_type","disease","country","discover","doctor","public_servant","record","specialize", "users"]
    choice = st.sidebar.selectbox("List of tables",menu)

#first table
    if choice=="disease_type":
        st.title("This is Disease Type table")
        st.subheader("View table")
        result2= db.view_all_data()
        df=pd.DataFrame(result2)
        st.dataframe(df,700)

        create_table()
        st.write("#")
        st.write("#")
        st.subheader("Add new instance")
        col1,col2=st.columns(2)
        with col1:
            id=st.number_input(f"Enter the id of the disease_type", min_value=0, format="%i")

        with col2:
            description= st.text_input('Please enter name')
        
        if st.button("Add Instance"):
            write_record(id,description,p_engine)
            st.success("Succesfully added disease type:{} with id {}".format(description,id))

        with st.expander("View Updated Data"):
            result = view_all_data()
            clean_df = pd.DataFrame(result)
            st.dataframe(clean_df,700)


        st.write("#")
        st.write("#")
        st.subheader("Update table")    
    

        list_of_ids = [i[0] for i in view_all_id()]
        selected_id = st.selectbox("Choose id",list_of_ids)
        result_description= get_description(selected_id)

        if selected_id:
            description = result_description[0][0]
  
            new_description= st.text_area("Changed description",description)
        
            if st.button("Update record"):
                update_record(new_description,selected_id)
                st.success("Updated row with id {} is changed to {}".format(selected_id,new_description))
            
            with st.expander("View Updated Data"):
                result = view_all_data()
                clean_df = pd.DataFrame(result)
                st.dataframe(clean_df,700)
    
        st.write("#")  
        st.write("#")  
        st.subheader("Delete record")   
        list_of_desc = [i[0] for i in view_all_desc()]
        selected_desc = st.selectbox("Choose description",list_of_desc)
        list_id=[i[0] for i in view_id(selected_desc)] 
        selected_id = st.selectbox("Choose description",list_id)          
        if st.button("Delete"):
            delete_record(selected_id,selected_desc)    
            st.success("Successfully deleted")

        with st.expander("View Updated Data"):
                result = view_all_data()
                clean_df = pd.DataFrame(result)
                st.dataframe(clean_df,700)
            

#second table
    if choice=="disease":
        st.title("This is Disease table")
        st.subheader("View table")
        result= db.view_all_data2()
        df=pd.DataFrame(result)
        st.dataframe(df,700)

        db.create_table2()
        st.write("#")
        st.write("#")
        st.subheader("Add new instance")
        col1,col2=st.columns(2)
        with col1:
            disease_code=st.text_input('Please enter disease_code')
            list_of_idss = [i[0] for i in db.view_all_id2()]
            selected_id = st.selectbox("Choose id",list_of_idss)

        with col2:
            pathogen= st.text_input('Please enter pathogen')
            description= st.text_input('Please enter description')
        
        if st.button("Add Instance"):
            db.write_record2(selected_id,description,pathogen, disease_code,p_engine)
            st.success("Succesfully added disease type:{} with id {}".format(disease_code,selected_id))

        with st.expander("View Updated Data"):
            result =db.view_all_data2()
            clean_df = pd.DataFrame(result)
            st.dataframe(clean_df,700)


        st.write("#")
        st.write("#")
        st.subheader("Update table")    
    

        list_of_codes = [i[0] for i in db.view_all_disease_code()]
        selected_code= st.selectbox("Choose disease_code",list_of_codes)
        result_row= db.get_row(selected_code)

        if selected_code:
            pathogen = result_row[0][1]
            description = result_row[0][2]
            id = result_row[0][3]

            col1,col2=st.columns(2)
            with col1:
                list_of_idsss = [i[0] for i in db.view_all_id()]
                new_id = st.selectbox("Choose id",list_of_idsss)
                new_pathogen= st.text_input('Please enter pathogen',pathogen)

            with col2:
                new_description= st.text_input('Please enter description',description)
                new_code= st.text_input('Please enter new disease_code',selected_code)
            if st.button("Update record"):
                db.update_record2(new_code,new_pathogen,new_description,new_id,selected_code)
                st.success("Record successfully updated")
            
            with st.expander("View Updated Data"):
                result = db.view_all_data2()
                clean_df = pd.DataFrame(result)
                st.dataframe(clean_df,700)
    
        st.write("#")  
        st.write("#")  
        st.subheader("Delete record")   
        selected_des = st.selectbox("Choose description",list_of_codes)   
        result_row= db.get_row(selected_code)
        clean_df = pd.DataFrame(result_row)
        st.dataframe(clean_df,700) 

        if st.button("Delete"):
            delete_record(selected_des)    
            st.success("Successfully deleted")

        with st.expander("View Updated Data"):
                result = db.view_all_data2()
                clean_df = pd.DataFrame(result)
                st.dataframe(clean_df,700)




#third table
    if choice=="doctor":
        st.title("This is Doctor table")
        st.subheader("View table")
        result= db.view_all_data4()
        df=pd.DataFrame(result)
        st.dataframe(df,700)

        db.create_table4()
        st.write("#")
        st.write("#")
        st.subheader("Add new instance")
        col1,col2=st.columns(2)
        with col1:
            list_of_emails = [i[0] for i in db.view_whole_email()]
            selected_email= st.selectbox("Choose email of doctor",list_of_emails)

        with col2:
            degree=st.text_input('Please enter degree')

            
        if st.button("Add Instance"):
            db.write_record4(email,degree,p_engine)
            st.success("Succesfully added doctor with email:{} who have degree {}".format(email,degree))



        with st.expander("View Updated Data"):
            result =db.view_all_data4()
            clean_df = pd.DataFrame(result)
            st.dataframe(clean_df,700)


        st.write("#")
        st.write("#")
        st.subheader("Update table")    
    

        list_of_emails = [i[0] for i in db.view_doctor_emails()]
        selected_email= st.selectbox("Choose email",list_of_emails)
        result_row= db.get_row4(selected_email)

        if selected_email:
            degree = result_row[0][1]

            new_degree= st.text_input('Choose degree',degree)

            if st.button("Update record"):
                db.update_record4(selected_email,new_degree)
                st.success("Record successfully updated")
            
            with st.expander("View Updated Data"):
                result = db.view_all_data4()
                clean_df = pd.DataFrame(result)
                st.dataframe(clean_df,700)
    
        st.write("#")  
        st.write("#")  
        st.subheader("Delete record")   
        selected_count= st.selectbox("Please choose email to delete",list_of_emails)  
        result_row= db.get_row4(selected_count)
        clean_df = pd.DataFrame(result_row)
        st.dataframe(clean_df,700)
         
        if st.button("Delete"):
            db.delete_record4(selected_count)    
            st.success("Successfully deleted")

        with st.expander("View Updated Data"):
                result = db.view_all_data4()
                clean_df = pd.DataFrame(result)
                st.dataframe(clean_df,700)

#forth table
    if choice=="country":
        st.title("This is Country table")
        st.subheader("View table")
        result= db.view_all_data3()
        df=pd.DataFrame(result)
        st.dataframe(df,700)

        db.create_table3()
        st.write("#")
        st.write("#")
        st.subheader("Add new instance")
        col1,col2=st.columns(2)
        with col1:
            country=st.text_input('Please enter country')

        with col2:
            population= st.number_input(f"Enter the population", min_value=0, format="%i")

            
        if st.button("Add Instance"):
            db.write_record3(country,population,p_engine)
            st.success("Succesfully added country:{} with population {}".format(country,population))



        with st.expander("View Updated Data"):
            result =db.view_all_data3()
            clean_df = pd.DataFrame(result)
            st.dataframe(clean_df,700)


        st.write("#")
        st.write("#")
        st.subheader("Update table")    
    

        list_of_countries = [i[0] for i in db.view_all_countries()]
        selected_country= st.selectbox("Choose country",list_of_countries)
        result_row3= db.get_row3(selected_country)

        if selected_country:
            population = result_row3[0][1]

            new_population= st.number_input(f"Enter the population", min_value=0, value=population, format="%i")

            if st.button("Update record"):
                db.update_record3(selected_country,new_population)
                st.success("Record successfully updated")
            
            with st.expander("View Updated Data"):
                result = db.view_all_data3()
                clean_df = pd.DataFrame(result)
                st.dataframe(clean_df,700)
    
        st.write("#")  
        st.write("#")  
        st.subheader("Delete record")   
        selected_count= st.selectbox("Choose country to delete",list_of_countries)  
        result_row= db.get_row3(selected_count)
        clean_df = pd.DataFrame(result_row)
        st.dataframe(clean_df,700)
         
        if st.button("Delete"):
            db.delete_record3(selected_count)    
            st.success("Successfully deleted")

        with st.expander("View Updated Data"):
                result = db.view_all_data3()
                clean_df = pd.DataFrame(result)
                st.dataframe(clean_df,700)


#fifth table
    if choice=="users":
        st.title("This is Users table")
        st.subheader("View table")
        result= db.view_all_data5()
        df=pd.DataFrame(result)
        st.dataframe(df,700)

        db.create_table5()
        st.write("#")
        st.write("#")
        st.subheader("Add new instance")
        col1,col2=st.columns(2)
        with col1:
            email=st.text_input('Please enter email of the user')
            name=st.text_input('Please enter name of the user')
            surname=st.text_input('Please enter surname of the user')

        with col2:
            salary= st.number_input(f"Enter the salary", min_value=0, format="%i")
            phone= st.number_input(f"Enter the phone", min_value=0, format="%i")
            list_of_countries = [i[0] for i in db.view_all_countries()]
            new_cname= st.selectbox("Choose country",list_of_countries)

        if st.button("Add Instance"):
            db.write_record5(email,name,surname,salary,phone,new_cname,p_engine)
            st.success("Succesfully added user:{}  {}".format(name,surname))

        with st.expander("View Updated Data"):
            result =db.view_all_data5()
            clean_df = pd.DataFrame(result)
            st.dataframe(clean_df,700)


        st.write("#")
        st.write("#")
        st.subheader("Update table")    
    

        list_of_allemails = [i[0] for i in db.view_whole_email()]
        selected_email= st.selectbox("Choose email",list_of_allemails)
        result_row= db.get_row5(selected_email)

        if selected_email:
            name = result_row[0][1]
            surname = result_row[0][2]
            salary = result_row[0][3]
            phone = result_row[0][4]

            col1,col2=st.columns(2)
            with col1:
                email=st.text_input('Please enter email of the user',selected_email)
                name=st.text_input('Please enter name of the user',name)
                surname=st.text_input('Please enter surname of the user',surname)

            with col2:
                salary= st.number_input(f"Enter the new salary", min_value=0, value=salary, format="%i")
                phone= st.text_input('Please enter surname of the user',phone)
                list_of_countries = [i[0] for i in db.view_all_countries()]
                new_cname= st.selectbox("Choose new country",list_of_countries)
            
            if st.button("Update record"):
                db.update_record5(selected_email,name,surname,salary,phone,new_cname)
                st.success("Record successfully updated")
            
        
            with st.expander("View Updated Data"):
                result = db.view_all_data5()
                clean_df = pd.DataFrame(result)
                st.dataframe(clean_df,700)
    

        st.write("#")  
        st.write("#")  
        st.subheader("Delete record")   
        selected_email = st.selectbox("Choose email to delete",list_of_allemails)   
        result_row= db.get_row5(selected_email)
        clean_df = pd.DataFrame(result_row)
        st.dataframe(clean_df,700) 

        if st.button("Delete"):
            db.delete_record5(selected_email)    
            st.success("Successfully deleted")

        with st.expander("View Updated Data"):
                result = db.view_all_data5()
                clean_df = pd.DataFrame(result)
                st.dataframe(clean_df,700)

#6th table
    if choice=="public_servant":
        st.title("This is Public Servant table")
        st.subheader("View table")
        result= db.view_all_data6()
        df=pd.DataFrame(result)
        st.dataframe(df,700)

        db.create_table6()
        st.write("#")
        st.write("#")
        st.subheader("Add new instance")
        col1,col2=st.columns(2)
        with col1:
            list_of_emails = [i[0] for i in db.view_whole_email()]
            selected_email= st.selectbox("Choose email of doctor",list_of_emails)

        with col2:
            department=st.text_input('Enter department with number of workers as Dept4 20')

            
        if st.button("Add Instance"):
            db.write_record6(selected_email,department,p_engine)
            st.success("Succesfully added public servant with email:{} who works in Department {}".format(selected_email,department))



        with st.expander("View Updated Data"):
            result =db.view_all_data6()
            clean_df = pd.DataFrame(result)
            st.dataframe(clean_df,700)


        st.write("#")
        st.write("#")
        st.subheader("Update table")    
    

        list_of_emails = [i[0] for i in db.view_all_emails()]
        selected_email= st.selectbox("Choose email",list_of_emails)
        result_row= db.get_row6(selected_email)

        if selected_email:
            department = result_row[0][1]

            new_department= st.text_input('Choose department',department)

            if st.button("Update record"):
                db.update_record6(selected_email,new_department)
                st.success("Record successfully updated")
            
            with st.expander("View Updated Data"):
                result = db.view_all_data6()
                clean_df = pd.DataFrame(result)
                st.dataframe(clean_df,700)
    
        st.write("#")  
        st.write("#")  
        st.subheader("Delete record")   
        selected_count= st.selectbox("Please choose email to delete",list_of_emails)  
        result_row= db.get_row6(selected_count)
        clean_df = pd.DataFrame(result_row)
        st.dataframe(clean_df,700)
         
        if st.button("Delete"):
            db.delete_record6(selected_count)    
            st.success("Successfully deleted")

        with st.expander("View Updated Data"):
                result = db.view_all_data6()
                clean_df = pd.DataFrame(result)
                st.dataframe(clean_df,700)

#7th table
    if choice=="specialize":
        st.title("This is Specialize table")
        st.subheader("View table")
        result= db.view_all_data7()
        df=pd.DataFrame(result)
        st.dataframe(df,700)

        db.create_table7()
        st.write("#")
        st.write("#")
        st.subheader("Add new instance")
        col1,col2=st.columns(2)
        with col1:
            list_of_emails = [i[0] for i in db.view_doctor_emails()]
            selected_email= st.selectbox("Choose email",list_of_emails)

        with col2:
            list_of_ids = [i[0] for i in db.view_all_id()]
            selected_id= st.selectbox("Choose id",list_of_ids)

            
        if st.button("Add Instance"):
            db.write_record7(selected_id,selected_email,p_engine)
            st.success("Succesfully added")



        with st.expander("View Updated Data"):
            result =db.view_all_data7()
            clean_df = pd.DataFrame(result)
            st.dataframe(clean_df,700)


        st.write("#")
        st.write("#")
        st.subheader("Update table")    

        list_of_emails = [i[0] for i in db.view_spec_email()]
        selected_email= st.selectbox("Choose email to change",list_of_emails)
        result_row= db.get_row7(selected_email)
        selected_id=result_row[0][1]
        new_id= st.selectbox("Choose id to change",list_of_ids)

        if st.button("Update record"):
            db.update_record7(new_id,selected_email,selected_id)
            st.success("Record successfully updated")
        
        with st.expander("View Updated Data"):
                result = db.view_all_data7()
                clean_df = pd.DataFrame(result)
                st.dataframe(clean_df,700)
    
        st.write("#")  
        st.write("#")  
        st.subheader("Delete record")   
        list_of_emails = [i[0] for i in db.view_all_spec_emails()]
        selected_email= st.selectbox("Choose email to delete",list_of_emails)
        result_id= [i[0] for i in db.get_id7(selected_email)]
        selected_id=st.selectbox("Choose id",result_id)
        
    
         
        if st.button("Delete"):
            db.delete_record7(selected_email,int(selected_id))    
            st.success("Successfully deleted")

        with st.expander("View Updated Data"):
                result = db.view_all_data7()
                clean_df = pd.DataFrame(result)
                st.dataframe(clean_df,700)

#eight table
    if choice=="record":
        st.title("This is Record table")
        st.subheader("View table")
        result= db.view_all_data8()
        df=pd.DataFrame(result)
        st.dataframe(df,700)

        db.create_table8()
        st.write("#")
        st.write("#")
        st.subheader("Add new instance")
        col1,col2=st.columns(2)
        with col1:
            list_of_allemails = [i[0] for i in db.view_whole_email()]
            email= st.selectbox("Choose email",list_of_allemails)
            list_of_countries = [i[0] for i in db.view_all_countries()]
            cname= st.selectbox("Choose country",list_of_countries)
            list_of_codes = [i[0] for i in db.view_all_disease_code()]
            disease_code= st.selectbox("Choose disease_code",list_of_codes)

        with col2:
            total_d =st.number_input(f"Enter the total_death", min_value=0, format="%i")
            total_p= st.number_input(f"Enter the total_patients", min_value=0, format="%i")

        if st.button("Add Instance"):
            db.write_record8(email,cname,disease_code, total_d,total_p,p_engine)
            st.success("Succesfully added record")

        with st.expander("View Updated Data"):
            result =db.view_all_data8()
            clean_df = pd.DataFrame(result)
            st.dataframe(clean_df,700)


        st.write("#")
        st.write("#")
        st.subheader("Update table")    
    

        col1,col2=st.columns(2)
        with col1:
            list_of_allemails = [i[0] for i in db.view_record_emails()]
            selected_email= st.selectbox("Choose email to change",list_of_allemails)
            list_of_cnames = [i[0] for i in db.view_record_cname(selected_email)]
            cname= st.selectbox("Choose country to change",list_of_cnames)
            list_of_code = [i[0] for i in db.view_record_code(selected_email,cname)]
            cname= st.selectbox("Choose disease to change",list_of_code)

                 

        with col2:
            total_death = st.number_input(f"Enter the new total deaths", min_value=0, format="%i")
            total_patients = st.number_input(f"Enter the new total patients", min_value=0, format="%i")
            
        if st.button("Update record"):
            db.update_record8(email,cname,disease_code,total_death,total_patients)
            st.success("Record successfully updated")
            
        
            with st.expander("View Updated Data"):
                result = db.view_all_data8()
                clean_df = pd.DataFrame(result)
                st.dataframe(clean_df,700)
    

        st.write("#")  
        st.write("#")  
        st.subheader("Delete record")   
        list_of_allemails = [i[0] for i in db.view_record_emails()]
        selected_email= st.selectbox("Choose email",list_of_allemails)
        list_of_cnames = [i[0] for i in db.view_record_cname(selected_email)]
        cname= st.selectbox("Choose country",list_of_cnames)
        list_of_code = [i[0] for i in db.view_record_code(selected_email,cname)]
        disease_code= st.selectbox("Choose disease",list_of_code)
        result_row=db.get_row8(selected_email,cname,disease_code)
        clean_df = pd.DataFrame(result_row)
        st.dataframe(clean_df,700) 

        if st.button("Delete"):
            db.delete_record8(selected_email,cname,disease_code)    
            st.success("Successfully deleted")

        with st.expander("View Updated Data"):
                result = db.view_all_data8()
                clean_df = pd.DataFrame(result)
                st.dataframe(clean_df,700)

#9table
    if choice=="discover":
        st.title("This is Discover table")
        st.subheader("View table")
        result= db.view_all_data9()
        df=pd.DataFrame(result)
        st.dataframe(df,700)

        db.create_table9()
        st.write("#")
        st.write("#")
        st.subheader("Add new instance")
        col1,col2=st.columns(2)
        with col1:
            list_of_countries = [i[0] for i in db.view_all_countries()]
            cname= st.selectbox("Choose country",list_of_countries)
            list_of_codes = [i[0] for i in db.view_all_disease_code()]
            disease_code= st.selectbox("Choose disease_code",list_of_codes)

        with col2:
            first_enc_date=st.date_input ("Enter first enc date")

        if st.button("Add Instance"):
            db.write_record9(cname,disease_code,first_enc_date, p_engine)
            st.success("Succesfully added record")

        with st.expander("View Updated Data"):
            result =db.view_all_data9()
            clean_df = pd.DataFrame(result)
            st.dataframe(clean_df,700)


        st.write("#")
        st.write("#")
        st.subheader("Update table")    
    

        col1,col2=st.columns(2)
        with col1:
            list_of_cnames = [i[0] for i in db.view_discover_cname()]
            cname= st.selectbox("Choose country to change",list_of_cnames)
            list_of_code = [i[0] for i in db.view_discover_code(cname)]
            disease_code= st.selectbox("Choose disease to change",list_of_code)        

        with col2:
            first_enc_date =st.date_input ("Enter new first enc date")
            
            
        if st.button("Update record"):
            db.update_record9(cname,disease_code,first_enc_date)
            st.success("Record successfully updated")
            
        
        with st.expander("View Updated Data"):
            result = db.view_all_data9()
            clean_df = pd.DataFrame(result)
            st.dataframe(clean_df,700)
    

        st.write("#")  
        st.write("#")  
        st.subheader("Delete record")   
        cname= st.selectbox("Choose country to delete",list_of_cnames)
        list_of_code = [i[0] for i in db.view_discover_code(cname)]
        disease_code= st.selectbox("Choose disease to delete",list_of_code)  
        result_row=db.get_row9(cname,disease_code)
        clean_df = pd.DataFrame(result_row)
        st.dataframe(clean_df,700) 

        if st.button("Delete"):
            db.delete_record9(cname,disease_code)    
            st.success("Successfully deleted")

        with st.expander("View Updated Data"):
                result = db.view_all_data9()
                clean_df = pd.DataFrame(result)
                st.dataframe(clean_df,700)


if __name__ == '__main__':
    main()