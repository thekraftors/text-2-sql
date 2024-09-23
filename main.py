from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

# Load the model and tokenizer
model_name = "thekraftors/Text_to_SQL22"
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Example input
text = "What are the total sales for the last month?"

# Tokenize the input text
inputs = tokenizer(text, return_tensors="pt")

# Generate SQL query
outputs = model.generate(**inputs)

# Decode the generated SQL query
sql_query = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(sql_query)
