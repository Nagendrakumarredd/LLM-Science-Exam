# Load the T5 tokenizer
tokenizer = T5Tokenizer.from_pretrained('t5-small')

# Load the T5 model
model = T5ForConditionalGeneration.from_pretrained('t5-small')
model.to(device)

from transformers import T5Tokenizer
tokenizer = T5Tokenizer.from_pretrained('t5-small')
inputs = tokenizer(format_input(test, 0), return_tensors="pt").to(device)
outputs = model.generate(**inputs)
answer = tokenizer.batch_decode(outputs, skip_special_tokens=True)

print(answer)
