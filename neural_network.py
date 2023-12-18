import numpy as np
import matplotlib.pyplot as plt


np.random.seed(20)
sample_s1 = np.random.normal(np.array([1, 3]), np.array([0.1, 0.3]), (1000, 2))
sample_s2 = np.random.normal(np.array([3, 1]), np.array([0.1, 0.3]), (1000, 2))
sample_1 = np.zeros([2000, 2])
sample_1_ss = np.zeros([2000, 2])
for i in range(len(sample_1)):
    if i % 2 == 0:
        sample_1[i, :] = sample_s1[i // 2, :]
    else:
        sample_1[i, :] = sample_s2[i // 2, :]
sample_1_ss[:, 0] = (sample_1[:, 0] - sample_1[:, 0].mean()) / sample_1[:, 0].std()
for i in range(len(sample_1)):
    if i % 2 == 0:
        sample_1_ss[i, 1] = (sample_1[i, 1] - sample_1[:, 1].mean()) / (
            sample_1[:, 1].std()
        )
    else:
        sample_1_ss[i, 1] = (sample_1[i, 1] - sample_1[:, 1].mean()) / (
            sample_1[:, 1].std()
        ) + 1


class logregBGDbackpropagation:
    """
    This class is suitable for classification
    """

    def __init__(self, x_train, y_train, epoch, learning_rate, random_seed):
        self.x_train = x_train.reshape(x_train.shape[0], -1)
        self.y_train = y_train.reshape(y_train.shape[0], -1)
        self.epoch = epoch
        self.learning_rate = learning_rate
        self.random_seed = random_seed
        self.n_dim_feature = np.size(self.x_train, axis=1)
        self.m_sample = np.size(self.x_train, axis=0)
        self.x_train_m = np.zeros([self.m_sample, self.n_dim_feature + 1])
        self.init_weight = np.zeros([self.n_dim_feature + 1, 1])
        self.weight = np.zeros([self.n_dim_feature + 1, 1])
        self.y_hat = np.zeros([self.m_sample, 1])
        self.score_y = np.zeros([self.m_sample, 1])
        self.score_y_d = np.zeros([self.m_sample, 1])
        self.diff_loss_f_score_y = np.zeros([self.m_sample, 1])
        self.diff_score_y_d_score_y = np.zeros([self.m_sample, 1])
        self.diff_y_hat_wj = np.zeros([self.n_dim_feature + 1, 1])
        self.treshold = 0
        self.loss_f = 0

    def run(self):
        self.add_dummy_n()
        self.initilzia_weight()
        for _ in range(self.epoch):
            self.build_model()
            self.acitivtion_function()
            self.decision_treshold()
            self.loss_function()
            self.back_propation()
            self.BGDecent()
            # x = np.linspace(-1.5, 1.5, 100)
            # plt.scatter(self.x_train[0::2], self.y_train[0::2], color="green")
            # plt.scatter(self.x_train[1::2], self.y_train[1::2], color="purple")
            # plt.plot(x, self.weight[0, 0]+self.weight[1, 0]*x)
            # plt.show()
        return self.weight

    def add_dummy_n(self):
        self.x_train_m = np.c_[np.ones(self.m_sample), self.x_train]

    def initilzia_weight(self):
        np.random.seed(self.random_seed)
        self.init_weight = np.random.randn(self.n_dim_feature + 1)
        if (self.weight == np.zeros(self.n_dim_feature + 1)).all:
            print((self.weight == np.zeros(self.n_dim_feature + 1)).all)
            self.weight[:, 0] = self.init_weight

    def build_model(self):
        self.y_hat = self.x_train_m @ self.weight

    def acitivtion_function(self):
        self.score_y = 1 / (1 + np.exp(-self.y_hat))

    def decision_treshold(self):
        self.treshold = self.score_y.mean()
        for j, _ in enumerate(self.score_y):
            if self.score_y[j] < 0.5:
                self.score_y_d[j, 0] = 0.001
            else:
                self.score_y_d[j, 0] = 0.999

    def loss_function(self):
        self.loss_f = -(1 / len(self.score_y)) * np.sum(
            self.y_train * np.log2(self.score_y_d)
            + (1 - self.y_train) * np.log2(1 - self.score_y_d)
        )
        print(self.loss_f)

    def back_propation(self):
        self.diff_loss_f_score_y = (self.y_train - self.score_y_d) / (
            len(self.score_y) * self.score_y_d * (self.score_y_d - 1) * np.log(2)
        )
        self.diff_score_y_d_score_y = self.score_y * (self.score_y - 1)
        self.diff_y_hat_wj = self.x_train_m

    def BGDecent(self):
        self.weight -= (
            -(1 / (len(self.score_y)))
            * (
                (self.epoch * self.diff_loss_f_score_y * self.diff_score_y_d_score_y).T
                @ (self.diff_y_hat_wj)
            )
        ).T
        # print(self.weight)


# from neural_network import logregBGDbackpropagation
s = logregBGDbackpropagation(sample_1_ss[:, 0], sample_1_ss[:, 1], 100, 0.00001, 92)
aa = s.run()
x = np.linspace(-1, 4, 100)
plt.plot(x, aa[0, 0] + aa[1, 0] * x)
plt.scatter(sample_1_ss[:, 0][0::2], sample_1_ss[:, 1][0::2], color="black")
plt.scatter(sample_1_ss[:, 0][1::2], sample_1_ss[:, 1][1::2], color="red")
plt.scatter(sample_1[:, 0][0::2], sample_1[:, 1][0::2], color="black")
plt.scatter(sample_1[:, 0][1::2], sample_1[:, 1][1::2], color="red")
# plt.show()
bb_1 = [0.999 if x % 2 == 0 else 0.001 for x in range(2000)]
bb_0 = np.sum(
    -(1 / 2000)
    * (
        sample_1_ss[:, 1] * np.log2(bb_1)
        + (1 - sample_1_ss[:, 1]) * np.log2(np.ones(2000) - bb_1)
    )
)
print(bb_0)
