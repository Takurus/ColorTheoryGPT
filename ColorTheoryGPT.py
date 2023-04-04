import tensorflow as tf
from transformers import GPT2Tokenizer, TFGPT2LMHeadModel

# Load the text data for your book
with open('book_text.txt', 'r') as f:
    text_data = f.read()

# Preprocess and tokenize the text data
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
tokenized_data = tokenizer.encode(text_data)

# Define the GPT model architecture
model = TFGPT2LMHeadModel.from_pretrained('gpt2', pad_token_id=tokenizer.eos_token_id)

# Set up the training process
train_dataset = tf.data.Dataset.from_tensor_slices(tokenized_data)
train_dataset = train_dataset.map(lambda x: {'input_ids': x[:-1], 'labels': x[1:]})
train_dataset = train_dataset.shuffle(1000).batch(16).repeat(5)

optimizer = tf.keras.optimizers.Adam(learning_rate=1e-5)
model.compile(optimizer=optimizer, loss=model.compute_loss)

# Train the model on the text data
model.fit(train_dataset)

# Generate text from the trained model
prompt = "What is your favorite color??"
input_ids = tokenizer.encode(prompt, return_tensors='tf')
output = model.generate(input_ids, max_length=50)
generated_text = tokenizer.decode(output[0])
print(generated_text)
