def post_process(predictions):
    valid = set(['A', 'B', 'C', 'D', 'E'])
    if set(predictions).isdisjoint(valid):
        final_pred = 'A B C D E'
    else:
        final_pred = []
        for prediction in predictions:
            if prediction in valid:
                final_pred += prediction
        to_add = valid - set(final_pred)
        final_pred.extend(list(to_add))
        final_pred = ' '.join(final_pred)
        
    return final_pred

