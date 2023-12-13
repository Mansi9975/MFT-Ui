from flask import Flask ,render_template ,request
import yaml

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('mft.html')
@app.route('/saveBasicInfo', methods=['POST'])
def save_basic_info():
     inumber = request.form.get('inumber')
     role = request.form.get('role')
     template_version = 'v1',
     data2 = {
        'inumber': inumber,
        'role': role,
        'template_version': template_version,
        'flow_metadata':{
        'owner': request.form.get('owner'),
        'description': request.form.get('description'),
        'max_active_runs': request.form.get('max_active_runs'),
        'schedule': request.form.get('schedule'),
        'start_date': request.form.get('start_date'),
        'use_sources': request.form.get('use_sources'),
        'catchup': request.form.get('catchup'),
        'tags': request.form.get('tags'),
        },
        'error_handling':{
        'email_on_failure':request.form.get('email_on_failure'),
        'retries':request.form.get('retries'),
        'email':request.form.get('email'),
        }
        
        
       
    }
     with open('airflowDrag.yml', 'w') as file:
        yaml.dump(data2, file, default_flow_style=False)

     return render_template('drag.html')

@app.route('/save', methods=['POST'])
def save_data():
    
    data = {
        
             'Sources': {
                'source_type': request.form.get('source_type'),
                'application_name': request.form.get('application_name'),
            }
            
        
       
    }
    with open('airflowDrag.yml', 'a') as file:
        yaml.dump(data, file, default_flow_style=False)

    return render_template('drag.html')

@app.route('/saveDest', methods=['POST'])
def save_destination():
    
    data1 = {
        'Destinations': {
             'destination_type': request.form.get('destination_type'),
             'dest_application_name': request.form.get('dest_application_name'),
        }
       
    }
    with open('airflowDrag.yml', 'a') as file:
        yaml.dump(data1, file, default_flow_style=False)
        
    return render_template('drag.html')
    

    
   

if __name__ =='__main__':
    app.run(debug=True)

    