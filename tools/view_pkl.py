import pickle

with open('../output/tools/cfgs/kitti_models/pgrcnn/default/eval/epoch_80/val/default/result.pkl', 'rb') as f:
    data = pickle.load(f)

print(data)
