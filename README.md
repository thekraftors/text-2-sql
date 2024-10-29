
# Text-to-SQL Project

This project converts natural language queries into SQL commands using a pre-trained NLP model. 

## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Directory Structure](#directory-structure)
- [Configuration Files](#configuration-files)
- [Sample Query](#sample-query)

## Requirements
- Python 3.8 or later
- Libraries: See `requirements.txt`

## Installation

1. Clone this repository:
   ```bash
   git clone https://your-repo-link.git
   cd text-2-sql
   ```
   
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. To run the program:
   ```bash
   python3 main.py
   ```

2. This will load the necessary models and configuration files to convert natural language into SQL commands.

## Directory Structure

- `main.py`: The main script for executing the text-to-SQL conversion.
- `config.json`: Configuration file for the model.
- `models/`: Contains model files like `model.safetensors`.
- `requirements.txt`: Dependency file listing required packages.

## Configuration Files

- `config.json`: Model configuration file.
- `generation_config.json`: Specifies generation parameters.
- `tokenizer_config.json`: Tokenizer settings for converting text into tokens.
  
## Sample Query

After running `main.py`, input a natural language query. The model will return a generated SQL query. For example:

### Input
> "What is the total sales grouped by month?"

### Output
```sql
SELECT sum(T1.Sales) 
FROM sales AS T1 
JOIN order_items AS T2 ON T1.order_id = T2.Order_id 
GROUP BY T2.Date_of_month 
HAVING count(*) >= (SELECT count(T2.month) FROM orders);
```

## Troubleshooting
- Ensure all dependencies are installed as per `requirements.txt`.
- Verify the presence of model files in the specified paths.

## License
MIT License
