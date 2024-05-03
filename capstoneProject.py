import joblib
import tkinter

try:
    model = joblib.load("adaBoostModel.joblib")
except FileNotFoundError:
    print("File was not found")

brands = ["Adidas", "New Balance", "Nike", "Puma", "Reebok", "Under Armor"]
categories = ["Dress", "Jacket", "Jeans", "Shoes", "Sweater", "T-shirt"]
colors = ["Black", "Blue", "Green", "Red", "White", "Yellow"]
sizes = ["L", "M", "S", "XL", "XS", "XXL"]
materials = ["Cotton", "Denim", "Nylon", "Polyester", "Silk", "Wool"]

columns = {"Brand": brands, "Category": categories, "Color": colors, "Size": sizes, "Material": materials}


class MyGUI:
    def __init__(self):
        self.mainWindow = tkinter.Tk()
        self.mainWindow.title("Capstone Project")

        self.titleLabel = tkinter.Label(self.mainWindow, text="Capstone Project")
        self.titleLabel.grid(row=0, column=0, columnspan = 2)

        self.identificationLabel = tkinter.Label(self.mainWindow, text="Identification")
        self.identificationLabel.grid(row=1, column=1)

        self.identificationText = tkinter.Text(self.mainWindow, width=20, height=20)
        self.identificationText.grid(row=2, column=1, rowspan=7)

        self.calculateButton = tkinter.Button(self.mainWindow, text="Calculate", command = self.calculate_price)
        self.calculateButton.grid(row = 9, column=1)

        self.outputFrame = tkinter.Frame(self.mainWindow)

        self.outputLabel = tkinter.Label(self.outputFrame, text="Price: ")
        self.outputLabel.grid(row = 0, column = 0)

        self.outputText = tkinter.Text(self.outputFrame, width = 14, height = 1)
        self.outputText.grid(row = 0, column = 1)

        self.outputFrame.grid(row = 10, column = 1)

        inputs_list = ["List Brands", "Brand", "List Categories", "Category", "List Colors", "Color", "List Sizes"
                       , "Size", "List Materials", "Material"]

        self.entries = []

        for index in range(0, len(inputs_list), 2):
            frame = tkinter.Frame(self.mainWindow)
            button = tkinter.Button(self.mainWindow, text = inputs_list[index],
                                    command = lambda name = inputs_list[index + 1]: self.get_info(name))
            label = tkinter.Label(frame, text = f"{inputs_list[index + 1]}: ")
            entry = tkinter.Entry(frame, width = 7, name = inputs_list[index + 1].lower())
            self.entries.append(entry)

            button.grid(row=index + 1, column = 0, padx = 5, pady = 5)
            label.grid(row = 0, column = 0)
            entry.grid(row = 0, column = 1)
            frame.grid(row = index + 2, column = 0, padx = 5, pady = 5)

        tkinter.mainloop()

    def get_info(self, category: str):
        self.identificationText.delete("1.0", tkinter.END)

        chosen_column = columns[category]

        output_text = ""

        for index in range(len(chosen_column)):
            output_text += f"{index}: {chosen_column[index]}\n"

        self.identificationText.insert("1.0", output_text)

    def calculate_price(self):
        self.outputText.delete("1.0", tkinter.END)

        outputs = []
        for entry in self.entries:
            try:
                output = int(entry.get())
                if 0 <= output < len(columns[str(entry.winfo_name()).title()]):
                    outputs.append(output)
            except ValueError:
                print("Invalid entry")
        if len(outputs) == 5:
            result_text = int(model.predict([outputs])[0])
        else:
            result_text = "Invalid inputs"

        self.outputText.insert("1.0", result_text)


if __name__ == "__main__":
    myGUI = MyGUI()
