# DigiX--人口属性预测赛题  
### *决赛第4名*  
### *代码内注释，代码含顺序，无数据*  

### 赛题说明 智能手机已成为人们工作生活中不可或缺的伙伴，当今社会几乎所有“衣食住行”都可以通过一部手机来解决。手机作为一种能够同时提供视频、游戏、音乐、阅读、摄影功能的全功能综合移动载体，正在逐步取代传统媒介（如电视、个人电脑、MP3、照相机等）。在此背景下，如何通过智能化、个性化应用以及精准推送服务来提升用户体验是每个手机厂商孜孜以求的目标，而数据则是实现这一目标的基石。用户的人口属性（如性别、年龄、常驻地等）数据一方面可以被用于个性化推荐服务，提升用户体验，另一方面可以用于手机用户群画像分析，帮助厂商了解产品的人群定位，优化产品设计。年龄是用户人口属性的重要维度，本次比赛任务为根据用户的手机使用行为习惯来预估用户所处的年龄段。每个用户（以唯一ID标识）对应唯一的年龄段。年龄段有6种划分，分别代表不同年龄段，分别为：小于等于18岁， 19-23岁， 24-34岁， 35-44岁， 45-54岁，大于等于55岁。参赛同学根据华为提供数据构建预测模型进行年龄段预估，在测试数据集上给出预估结果。  

文件分布：  
|-answer  
    |-submission.csv  
|-data  
    |-age_train.csv  
    |-age_test.csv  
    |-user_app_actived.csv  
    |-user_basic_info.csv  
    |-user_behavior_info.csv  
    |-user_app_usage.csv  
    |-app_info.csv  
    |-oneDayUsage  
        |-2019-03-10.csv  
        |-2019-03-16.csv  
|-model  
    |-  
|-processed  
    |-importance_app_inActivate.csv  
    |-basicTrainData.csv  
    |-category_num.csv  
    |-important_app_rowIndex.csv  
    |-importance_app_inActivate.csv  
    |-user_app_train.csv  
    |-usageDuraTimes_Sum.csv  
|-src  
    |-appToCategory.ipynb  
    |-category_activated_4000.ipynb  
    |-getOneDayUsage.ipynb  
    |-usageDuraTimes_Sum.ipynb  
    |-basic_feature.ipynb  
    |-dealActived.ipynb  
    |-importAppInActivate.ipynb  
    |-usage_on_category.ipynb  
    |-top_appid_sum_times_usage.ipynb  
    |-30days_appid_usage.ipynb  
    |-XGBoost_complete-13100.ipynb  
    |-XGBoost_complete-15112.ipynb  
    |-CatBoost_K-fold_cross-validation-15112.ipynb  
    |-CatBoost_K-fold_cross-validation-13100.ipynb  
    |-CatBoost_K-fold_cross-validation-13100+15112.ipynb  
    |-RF_K-fold_cross-validation-softmax.ipynb  
    |-merge_dnn_xgboost_rf_stacking-Catboost.ipynb  
    |-NN_13100+15112-10000.ipynb  
    |-NN_13100+15112.ipynb  
    |-NN_13100.ipynb  
    |-NN_15112.ipynb  
    |-TI-DIF_Feature.ipynb  
|-trainTestData  
    |-trainData258.npz  
    |-testData258.npz  
    |-trainData9400.npz  
    |-trainData4000.npz  
    |-testData9400.npz  
    |-testData4000.npz  
    |-trainData752.npz  
    |-testData752.npz  
    |-trainData30.npz  
    |-testData30.npz  
    |-trainData60.npz  
    |-testData60.npz  
    |-trainData5000.npz  
    |-trainData5000.npz  
    |-trainData13100.npz  
    |-testData13100.npz  
    |-trainData15112.npz  
    |-testData15112.npz  
    |-usageCategory  
        |-usage_on_category201903010.csv  
        |-usage_on_category20190304.csv  
        |-usage_on_category20190306.csv  
        |-usage_on_category20190302.csv  
