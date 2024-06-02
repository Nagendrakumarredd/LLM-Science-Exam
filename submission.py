submission = pd.read_csv(
    data_path / 'sample_submission.csv', index_col='id')

for idx in test.index:
    inputs = tokenizer(format_input(test, idx), return_tensors="pt").to(device)
    outputs = model.generate(**inputs)
    answer = tokenizer.batch_decode(outputs, skip_special_tokens=True)
    submission.loc[idx, 'prediction'] = post_process(answer)

submission_file = 'submission.csv'  
submission.to_csv(submission_file, index=False)
print("Submission CSV file created and saved:", submission_file)


import pandas as pd

submission_file = 'submission.csv' 
submission_df = pd.read_csv(submission_file)
print(submission_df.head())
