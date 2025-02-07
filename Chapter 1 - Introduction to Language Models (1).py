# Databricks notebook source
# MAGIC %md
# MAGIC <h1>Chapter 1 - Introduction to Language Models</h1>
# MAGIC <i>Exploring the exciting field of Language AI</i>
# MAGIC
# MAGIC
# MAGIC <a href="https://www.amazon.com/Hands-Large-Language-Models-Understanding/dp/1098150961"><img src="https://img.shields.io/badge/Buy%20the%20Book!-grey?logo=amazon"></a>
# MAGIC <a href="https://www.oreilly.com/library/view/hands-on-large-language/9781098150952/"><img src="https://img.shields.io/badge/O'Reilly-white.svg?logo=data:image/svg%2bxml;base64,PHN2ZyB3aWR0aD0iMzQiIGhlaWdodD0iMjciIHZpZXdCb3g9IjAgMCAzNCAyNyIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGNpcmNsZSBjeD0iMTMiIGN5PSIxNCIgcj0iMTEiIHN0cm9rZT0iI0Q0MDEwMSIgc3Ryb2tlLXdpZHRoPSI0Ii8+CjxjaXJjbGUgY3g9IjMwLjUiIGN5PSIzLjUiIHI9IjMuNSIgZmlsbD0iI0Q0MDEwMSIvPgo8L3N2Zz4K"></a>
# MAGIC <a href="https://github.com/HandsOnLLM/Hands-On-Large-Language-Models"><img src="https://img.shields.io/badge/GitHub%20Repository-black?logo=github"></a>
# MAGIC [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/HandsOnLLM/Hands-On-Large-Language-Models/blob/main/chapter01/Chapter%201%20-%20Introduction%20to%20Language%20Models.ipynb)
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC This notebook is for Chapter 1 of the [Hands-On Large Language Models](https://www.amazon.com/Hands-Large-Language-Models-Understanding/dp/1098150961) book by [Jay Alammar](https://www.linkedin.com/in/jalammar) and [Maarten Grootendorst](https://www.linkedin.com/in/mgrootendorst/).
# MAGIC
# MAGIC ---
# MAGIC
# MAGIC <a href="https://www.amazon.com/Hands-Large-Language-Models-Understanding/dp/1098150961">
# MAGIC <img src="https://raw.githubusercontent.com/HandsOnLLM/Hands-On-Large-Language-Models/main/images/book_cover.png" width="350"/></a>
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### [OPTIONAL] - Installing Packages on <img src="https://colab.google/static/images/icons/colab.png" width=100>
# MAGIC
# MAGIC If you are viewing this notebook on Google Colab (or any other cloud vendor), you need to **uncomment and run** the following codeblock to install the dependencies for this chapter:

# COMMAND ----------

# MAGIC %md
# MAGIC ---
# MAGIC
# MAGIC 💡 **NOTE**: We will want to use a GPU to run the examples in this notebook. In Google Colab, go to
# MAGIC **Runtime > Change runtime type > Hardware accelerator > GPU > GPU type > T4**.
# MAGIC
# MAGIC ---

# COMMAND ----------

# %%capture
# !pip install transformers>=4.40.1 accelerate>=0.27.2

# COMMAND ----------

# MAGIC %md
# MAGIC # Phi-3
# MAGIC
# MAGIC The first step is to load our model onto the GPU for faster inference. Note that we load the model and tokenizer separately (although that isn't always necessary).

# COMMAND ----------

from transformers import AutoModelForCausalLM, AutoTokenizer

# Load model and tokenizer
model = AutoModelForCausalLM.from_pretrained(
    "microsoft/Phi-3-mini-4k-instruct",
    device_map="cuda",
    torch_dtype="auto",
    trust_remote_code=True,
)
tokenizer = AutoTokenizer.from_pretrained("microsoft/Phi-3-mini-4k-instruct")

# COMMAND ----------

# MAGIC %md
# MAGIC Although we can now use the model and tokenizer directly, it's much easier to wrap it in a `pipeline` object:

# COMMAND ----------

from transformers import pipeline

# Create a pipeline
generator = pipeline(
    "text-generation",
    model=model,
    tokenizer=tokenizer,
    return_full_text=False,
    max_new_tokens=500,
    do_sample=False
)

# COMMAND ----------

# MAGIC %md
# MAGIC Finally, we create our prompt as a user and give it to the model:

# COMMAND ----------

# The prompt (user input / query)
messages = [
    {"role": "user", "content": "Create a funny joke about chickens."}
]

# Generate output
output = generator(messages)
print(output[0]["generated_text"])
