from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)



colors = [
    {"background": "white", "color": "black"},
    {"background": "black", "color": "white"},
    {"background": "lightblue", "color": "red"}
]

color_index = 0  


@app.route("/", methods=["GET", "POST"])
def home():
    global color_index  # Hacemos que el índice sea global para mantener el estado
    
    # Si es POST (cuando enviamos el formulario)
    if request.method == "POST":
       
        color_index = (color_index + 1) % len(colors)
        text_input = request.form.get("textBox") 
        return render_template("index.html", text=text_input, color=colors[color_index])

    # Si es GET (cuando cargamos la página por primera vez)
    return render_template("index.html", text="", color=colors[color_index])

# Ejecutar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True)
