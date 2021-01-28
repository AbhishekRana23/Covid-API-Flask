from flask import Flask , jsonify
from covid import Covid

app = Flask(__name__)
app.url_map.strict_slashes = False

covid = Covid(source="worldometers")

@app.route('/')
def home():
    return "Hey There! Covid Api Is Functional"

@app.route('/all')
def getall():
    allcovid = covid.get_data()
    return jsonify({"query": "All", "Data": str(allcovid)})
  
@app.route('/<countryname>')
def covidbycountry(countryname):
    try:            
        covidbycountry = covid.get_status_by_country_name(countryname)
        return jsonify({"query": countryname, "Data": str(covidbycountry)})
    except ValueError:
            return jsonify({"query": countryname, "Data": f"Invalid Country Name! {countryname}"})  

@app.route('/list')
def getcountries():
    countries = covid.list_countries()
    return jsonify({"query": "list", "Data": str(countries)})

@app.route('/world')
def allworld():
    active = covid.get_total_active_cases()
    confirmed = covid.get_total_confirmed_cases()
    recovered = covid.get_total_recovered()
    deaths = covid.get_total_deaths()
    return jsonify({"query": "world", "active": active, "confirmed": confirmed, "recovered": recovered, "Dealths": deaths})

if __name__ == "__main__":
    app.debug = True
    app.run("0.0.0.0",port=5000)    
