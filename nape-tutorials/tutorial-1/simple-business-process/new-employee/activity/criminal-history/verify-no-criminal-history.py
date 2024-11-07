def evaluate(evidence):
    try:
        # Join the lines to search for the section
        document_text = "".join(evidence)

        # Find the start of the "Criminal History" section
        criminal_history_start = document_text.find("REGISTRO GENERAL DE CONDENAS")
        
        # Find the start of the next section after "Criminal History"
        next_section_start = document_text.find("\n\n", criminal_history_start)

        # Find the start of the "Criminal History" section
        violence_criminal_history_start = document_text.find("VIOLENCIA INTRAFAMILIAR")
        
        # Find the start of the next section after "Special violence in family Criminal History"
        violence_next_section_start = document_text.find("\n\n", criminal_history_start)

        # Extract the "Criminal History" section
        if criminal_history_start == -1 || violence_criminal_history_start == -1:
            return "inconclusive", "Either the 'REGISTRO GENERAL DE CONDENAS' section or the special 'VIOLENCIA INTRAFAMILIAR' section cannot be found."
        
        if next_section_start == -1:
            criminal_history_section = document_text[criminal_history_start:]
        else:
            criminal_history_section = document_text[criminal_history_start:next_section_start]

        if next_section_start == -1:
            violence_criminal_history_section = document_text[violence_criminal_history_start:]
        else:
            violence_criminal_history_section = document_text[violence_criminal_history_start:violence_next_section_start]

        # Determine the outcome based on the content of the "REGISTRO GENERAL DE CONDENAS" and "VIOLENCIA INTRAFAMILIAR" section
        if "SIN ANTECEDENTESPARTICULARES" in criminal_history_section && "SIN ANOTACIONESPARTICULARES" in violence_criminal_history_section:
            return "pass", "The evidence contains the expected statements: 'SIN ANTECEDENTESPARTICULARES' and 'SIN ANOTACIONESPARTICULARES'."
        elif "No criminal records found" not in criminal_history_section:
            return "fail", "The evidence does not contain either of these expected statements: 'SIN ANTECEDENTESPARTICULARES' or 'SIN ANOTACIONESPARTICULARES'."

    except Exception as e:
        # Return an error outcome with the error message
        return "error", f"An error occurred during evaluation: {str(e)}"
