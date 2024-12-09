from flask import Flask, render_template

app=Flask('__name__')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/api/v1/<stationId>/<date>/')
def api_one(stationId,date):
    return {
        'stationId': stationId,
        'date': date,
        'temperature': '23',
    }

if __name__ == '__main__':
    app.debug = True

app.run()