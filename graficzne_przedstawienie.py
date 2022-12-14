import dash
import dash_bio as dashbio
from dash import html
import urllib.request as urlreq
from dash.dependencies import Input, Output
from Bio import SeqIO

app = dash.Dash(__name__)

data = urlreq.urlopen(
    'https://raw.githubusercontent.com/Arjissuan/tunneling_project/master/viever.fasta'
).read().decode('utf-8')
app.layout = html.Div([
    dashbio.AlignmentChart(
        id='viewer',
        data=data,
        height=900,
        tilewidth=30,
    ),
    html.Div(id='default-alignment-viewer-output')
])

@app.callback(
    Output('output', 'children'),
    Input('viewer', 'eventDatum')
)
def update_output(value):
    if value is None:
        return 'No data.'
    return str(value)

if __name__ == '__main__':
    app.run_server(debug=True)