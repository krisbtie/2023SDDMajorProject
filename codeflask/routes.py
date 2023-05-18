from codeflask import app
from flask import render_template

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html',title='Home')

@app.route('/assistance')
def assistance():
# load the Bokeh plot HTML file
    bokehHtmlFile = open('codeflask/templates/assistanceByNeedForAssistance.html', 'r')
    plot_html = bokehHtmlFile.read()
    return render_template('assistance.html',title='Assistance',plot_html=plot_html)

@app.route('/education')
def education():
# load the Bokeh plot HTML file
    bokehHtmlFile = open('codeflask/templates/educationByInstBySex.html', 'r')
    plot_html = bokehHtmlFile.read()
    return render_template('education.html',title='Education',plot_html=plot_html)

@app.route('/population')
def population():
# load the Bokeh plot HTML file
    bokehHtmlFile = open('codeflask/templates/populationByGeneration.html', 'r')
    plot_html = bokehHtmlFile.read()
    bokehHtmlFile2 = open('codeflask/templates/populationByState.html', 'r')
    plot_html2 = bokehHtmlFile2.read()
    bokehHtmlFile3 = open('codeflask/templates/populationByAgegrpBySex.html', 'r')
    plot_html3 = bokehHtmlFile3.read()
    return render_template('population.html', title='Population', plot_html=plot_html, plot_html2=plot_html2, plot_html3=plot_html3)









