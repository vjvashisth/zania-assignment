# Web Interface

import panel as pn

pn.extension('texteditor', template="bootstrap", sizing_mode='stretch_width')
pn.state.template.param.update(
    main_max_width="690px",
    header_background="#F08080",
)

file_input = pn.widgets.FileInput(width=300)

openaikey = pn.widgets.PasswordInput(
    value="", placeholder="Enter API key", width=300
)
prompt = pn.widgets.TextEditor(
    value="", placeholder="Type your question", height=160, toolbar=False
)
run_button = pn.widgets.Button(name="Run!")

convos = []  # store all panel objects in a list

def qa_result(_):
    os.environ["OPENAI_API_KEY"] = openaikey.value
    
    # save pdf file to a temp file 
    if file_input.value is not None:
        file_input.save("/.cache/temp.pdf")
    
        prompt_text = prompt.value
        if prompt_text:
            result = main(file="/.cache/temp.pdf", query=prompt_text, questions, slack_token, slack_channel)
            convos.extend([
                pn.Row(
                    pn.panel("\U0001F60A", width=10),
                    prompt_text,
                    width=600
                ),
                pn.Row(
                    pn.panel("\U0001F916", width=10),
                    pn.Column(
                        result["result"],
                        "Relevant source text:",
                        pn.pane.Markdown('\n--------------------------------------------------------------------\n'.join(doc.page_content for doc in result["source_documents"]))
                    )
                )
            ])
    return pn.Column(*convos, margin=15, width=575, min_height=400)

qa_interactive = pn.panel(
    pn.bind(qa_result, run_button),
    loading_indicator=True,
)

output = pn.WidgetBox('*Output will show up here:*', qa_interactive, width=670, scroll=True)

# layout
pn.Column(
    pn.pane.Markdown("""
    ## Zania Assignment
    
    1) Upload Handbook 2) Enter API key 3) Type A question and click "Run"
    
    """),
    pn.Row(file_input,openaikey),
    output,
    widgets

).servable()
