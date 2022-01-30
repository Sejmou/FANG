import json
import random

if __name__ == '__main__':
    """
    Modifies the hardcoded split by reshuffling its contents
    Before rerunning FANG the new split file must be renamed to match the original
    but it is highly recommended to keep the original file saved somewhere to not lose it
    """
    filename = "train_test_10"
    resultname = "train_test_10_modified"
    with open(f"../data/news_graph/{filename}.json") as f:
        content = json.load(f)
        train = len(content['train'])
        val = len(content['val'])
        test = len(content['test'])
        n = train + val + test
        all = content['train'] + content['val'] + content['test']

        t = random.sample(range(len(all)), train)
        new_train = [x for i, x in enumerate(all) if i in t]
        tmp = [x for i, x in enumerate(all) if i not in t]
        all = tmp

        t = random.sample(range(len(all)), val)
        new_val = [x for i, x in enumerate(all) if i in t]
        tmp = [x for i, x in enumerate(all) if i not in t]
        all = tmp

        new_test = all

        result = {'train': new_train, 'val': new_val, 'test': new_test}
        with open(f"../data/news_graph/{resultname}.json", 'w') as r:
            json.dump(result, r)

