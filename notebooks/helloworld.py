from spider.stock_spider import main as stock_spider_main
from algorithm.RL.DoubleDQN import main as model_main


# stock_spider_main({
#     "codes" : ["002303"],
#     "start" : "2008-01-01",
#     "end":"2018-01-01"
# })

model_main({
    "mode" : "train",
    "codes" : ["002303"],
    "market" : "stock",
    "episode"  : 2000,
    "training_data_ratio" : 0.5
})