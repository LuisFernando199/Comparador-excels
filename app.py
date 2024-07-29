from flask import Flask, request, render_template, redirect, url_for
import pandas as pd
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    if 'file1' not in request.files or 'file2' not in request.files:
        return redirect(request.url)

    file1 = request.files['file1']
    file2 = request.files['file2']

    if file1.filename == '' or file2.filename == '':
        return redirect(request.url)

    filepath1 = os.path.join(app.config['UPLOAD_FOLDER'], file1.filename)
    filepath2 = os.path.join(app.config['UPLOAD_FOLDER'], file2.filename)

    file1.save(filepath1)
    file2.save(filepath2)

    # Leer los archivos Excel
    excel1 = pd.ExcelFile(filepath1)
    excel2 = pd.ExcelFile(filepath2)

    differences = compare_excel_files(excel1, excel2)

    return render_template('result.html', differences=differences)

def compare_excel_files(excel1, excel2):
    if set(excel1.sheet_names) != set(excel2.sheet_names):
        return "Los archivos tienen diferentes hojas."

    differences = []

    for sheet in excel1.sheet_names:
        df1 = pd.read_excel(excel1, sheet_name=sheet)
        df2 = pd.read_excel(excel2, sheet_name=sheet)

        if df1.equals(df2):
            differences.append(f"Hoja '{sheet}': Los archivos son iguales.")
        else:
            for i in range(len(df1)):
                for j in range(len(df1.columns)):
                    if df1.iat[i, j] != df2.iat[i, j]:
                        differences.append(f"Hoja '{sheet}' - Diferencia en fila {i+1}, columna {j+1}: {df1.iat[i, j]} != {df2.iat[i, j]}")

    return differences

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    app.run(debug=True)
