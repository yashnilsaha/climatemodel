from flask import Flask, render_template,send_file, make_response
import os
from plotting import get_surface_change_plot_as_bytes
from plotting import get_forecast_surface_change_plot_as_bytes
from plotting import get_global_carbon_dioxide_change_plot_as_bytes
from plotting import get_global_forecast_carbon_dioxide_change_plot_as_bytes
from plotting import get_usa_carbon_dioxide_change_plot_as_bytes
from plotting import get_china_carbon_dioxide_change_plot_as_bytes
from plotting import get_india_carbon_dioxide_change_plot_as_bytes
from plotting import get_uk_carbon_dioxide_change_plot_as_bytes
from plotting import get_australia_carbon_dioxide_change_plot_as_bytes
from plotting import get_japan_carbon_dioxide_change_plot_as_bytes
from plotting import get_germany_carbon_dioxide_change_plot_as_bytes
from plotting import get_nigeria_carbon_dioxide_change_plot_as_bytes
from plotting import get_brazil_carbon_dioxide_change_plot_as_bytes
from plotting import get_carbon_offset_plot_as_bytes

app = Flask(__name__)

env = os.getenv("run_env", "dev")

if env == "dev":
    BASE_URL = "http://localhost:5000/"


# two decorators, same function
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html', the_title='My Climate Model')

@app.route('/carbon.html')
def carbon():
    return render_template('carbon.html', the_title='Carbon Dioxide Emission Analysis')

@app.route('/temp.html')
def temp():
    return render_template('temp.html', the_title='Temperature Anomaly Analysis')

@app.route('/carbon_offset.html')
def carbon_offset():
    return render_template('carbon_offset.html', the_title='Carbon Offset via Trees')
    
    
@app.route('/plots/global_surface_change', methods=['GET'])
def global_surface_change():
    try:
        bytes_obj = get_surface_change_plot_as_bytes()
        return send_file(bytes_obj,attachment_filename='plot1.png',mimetype='image/png')
    
    except ValueError:
        # something went wrong to return bad request
        return make_response('Unsupported request', 400)

@app.route('/plots/global_forecast_surface_change', methods=['GET'])
def global_forecast_surface_change():
    try:
        bytes_obj_forecast = get_forecast_surface_change_plot_as_bytes()
        return send_file(bytes_obj_forecast,attachment_filename='plot2.png',mimetype='image/png')
    
    except ValueError:
        # something went wrong to return bad request
        return make_response('Unsupported request', 400)

@app.route('/plots/usa_carbon_dioxide_analysis', methods=['GET'])        
def usa_carbon_dioxide_analysis():
    try:
        bytes_obj_usa = get_usa_carbon_dioxide_change_plot_as_bytes()
        return send_file(bytes_obj_usa,attachment_filename='usa.png',mimetype='image/png')
    
    except ValueError:
        # something went wrong to return bad request
        return make_response('Unsupported request', 400)        
        
@app.route('/plots/china_carbon_dioxide_analysis', methods=['GET'])        
def china_carbon_dioxide_analysis():
    try:
        bytes_obj_china = get_china_carbon_dioxide_change_plot_as_bytes()
        return send_file(bytes_obj_china,attachment_filename='china.png',mimetype='image/png')
    
    except ValueError:
        # something went wrong to return bad request
        return make_response('Unsupported request', 400)

@app.route('/plots/india_carbon_dioxide_analysis', methods=['GET'])        
def india_carbon_dioxide_analysis():
    try:
        bytes_obj_india = get_india_carbon_dioxide_change_plot_as_bytes()
        return send_file(bytes_obj_india,attachment_filename='india.png',mimetype='image/png')
    
    except ValueError:
        # something went wrong to return bad request
        return make_response('Unsupported request', 400)

@app.route('/plots/uk_carbon_dioxide_analysis', methods=['GET'])        
def uk_carbon_dioxide_analysis():
    try:
        bytes_obj_uk = get_uk_carbon_dioxide_change_plot_as_bytes()
        return send_file(bytes_obj_uk,attachment_filename='uk.png',mimetype='image/png')
    
    except ValueError:
        # something went wrong to return bad request
        return make_response('Unsupported request', 400)

@app.route('/plots/australia_carbon_dioxide_analysis', methods=['GET'])        
def australia_carbon_dioxide_analysis():
    try:
        bytes_obj_australia = get_australia_carbon_dioxide_change_plot_as_bytes()
        return send_file(bytes_obj_australia,attachment_filename='aus.png',mimetype='image/png')
    
    except ValueError:
        # something went wrong to return bad request
        return make_response('Unsupported request', 400)

@app.route('/plots/japan_carbon_dioxide_analysis', methods=['GET'])        
def japan_carbon_dioxide_analysis():
    try:
        bytes_obj_japan = get_japan_carbon_dioxide_change_plot_as_bytes()
        return send_file(bytes_obj_japan,attachment_filename='japan.png',mimetype='image/png')
    
    except ValueError:
        # something went wrong to return bad request
        return make_response('Unsupported request', 400)

@app.route('/plots/germany_carbon_dioxide_analysis', methods=['GET'])        
def germany_carbon_dioxide_analysis():
    try:
        bytes_obj_germany = get_germany_carbon_dioxide_change_plot_as_bytes()
        return send_file(bytes_obj_germany,attachment_filename='germany.png',mimetype='image/png')
    
    except ValueError:
        # something went wrong to return bad request
        return make_response('Unsupported request', 400)

@app.route('/plots/nigeria_carbon_dioxide_analysis', methods=['GET'])        
def nigeria_carbon_dioxide_analysis():
    try:
        bytes_obj_nigeria = get_nigeria_carbon_dioxide_change_plot_as_bytes()
        return send_file(bytes_obj_nigeria,attachment_filename='nig.png10',mimetype='image/png')
    
    except ValueError:
        # something went wrong to return bad request
        return make_response('Unsupported request', 400)

@app.route('/plots/brazil_carbon_dioxide_analysis', methods=['GET'])        
def brazil_carbon_dioxide_analysis():
    try:
        bytes_obj_brazil = get_brazil_carbon_dioxide_change_plot_as_bytes()
        return send_file(bytes_obj_brazil,attachment_filename='brazil.png',mimetype='image/png')
    
    except ValueError:
        # something went wrong to return bad request
        return make_response('Unsupported request', 400)
    

@app.route('/plots/global_carbon_dioxide_analysis', methods=['GET'])        
def global_carbon_dioxide_analysis():
    try:
        bytes_obj_global = get_global_carbon_dioxide_change_plot_as_bytes()
        return send_file(bytes_obj_global,attachment_filename='world.png',mimetype='image/png')
    
    except ValueError:
        # something went wrong to return bad request
        return make_response('Unsupported request', 400)
    
@app.route('/plots/global_forecast_carbon_dioxide_analysis', methods=['GET'])        
def global_forecast_carbon_dioxide_analysis():
    try:
        bytes_obj_global_forecast = get_global_forecast_carbon_dioxide_change_plot_as_bytes()
        return send_file(bytes_obj_global_forecast,attachment_filename='world_forecast.png',mimetype='image/png')
    
    except ValueError:
        # something went wrong to return bad request
        return make_response('Unsupported request', 400)

@app.route('/plots/routeto_carbon_offset', methods=['GET'])        
def routeto_carbon_offset():
    try:
        bytes_carbon_offset = get_carbon_offset_plot_as_bytes()
        return send_file(bytes_carbon_offset,attachment_filename='carbon_offset.png',mimetype='image/png')
    
    except ValueError:
        # something went wrong to return bad request
        return make_response('Unsupported request', 400)   
        
if __name__ == '__main__':
    app.run(debug=False)
