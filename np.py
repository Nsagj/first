#https://github.com/hmmlearn/hmmlearn
#hmm��
#��Դ��https://blog.csdn.net/xinfeng2005/article/details/53939192
from hmmlearn.hmm import GaussianHMM
from hmmlearn.hmm import MultinomialHMM
#GaussianHMM����Թ۲�Ϊ���������Թ۲����B�ɸ�������״̬��Ӧ�۲�״̬�ĸ�˹�ֲ������ܶȺ�������������
#��ӦGMMHMMͬ������multinomialHMM�������ɢ�۲⣬B����ֱ�Ӹ���

############################################����ʵ��#######################
#�۲�״̬�Ƕ�ά��������״̬��4����
#������ǵġ�means��������4��24��2�ľ��󣬶���covars��������4��2��24��2��2������
import numpy as np
startprob=np.array([0.6, 0.3, 0.1, 0.0])
#����1,3֮����ת�ƿ��ܣ���Ӧ����Ϊ0��
transmat=np.array([[0.7, 0.2, 0.0, 0.1],
                     [0.3, 0.5, 0.2, 0.0],
                     [0.0, 0.3, 0.5, 0.2],
                     [0.2, 0.0, 0.2, 0.6]])
#����״̬��component����˹�ֲ���ֵ��The means of each component
means=np.array([[0.0,  0.0],
                  [0.0, 11.0],
                  [9.0, 10.0],
                  [11.0, -1.0]])
#����״̬Э����The covariance of each component
covars=.5*np.tile(np.identity(2),(4,1,1))
#np.tile(x,(n,m)),��x�ӵ�һ���Ḵ��n�����������ӵڶ����Ḵ��m�����������棬Ϊ1*2*2���������˾���4*2*2
#np.identity(n)��ȡnά��λ����np.eye(n.m.k)��ȡn��m�жԽ�Ԫ��ƫ��k�ĵ�λ��

# hmm=GaussianHMM(n_components=4,
# ����covariance_type��Ϊ"full":���еĦ�,������Ҫָ����ȡֵΪ��spherical���򦲵ķǶԽ���Ԫ��Ϊ0���Խ���Ԫ����ͬ��ȡֵΪ��diag���򦲵ķǶԽ���Ԫ��Ϊ0���Խ���Ԫ�ؿ��Բ�ͬ��"tied"ָ���е�����״̬��Ӧ�Ĺ۲�״̬�ֲ�ʹ����ͬ��Э�������
#                 covariance_type='full',
#                 startprob_prior=1.0,#PI
#                 transmat_prior=1.0,#״̬ת��A
#                 means_prior=,#��means��������ʾ��������״̬��Ӧ�ĸ�˹�ֲ������������γɵľ���
#                 means_weight=,
#                 covars_prior=,#��covars��������ʾ��������״̬��Ӧ�ĸ�˹�ֲ�Э��������γɵ���ά����
#                 covars_weight=,
#                 algorithm=,
#                 )
hmm=GaussianHMM(n_components=4,covariance_type='full')
#Instead of fitting it from the data, we directly set the estimated parameters, the means and covariance of the components
hmm.startprob_=startprob
hmm.transmat_=transmat
hmm.means_=means
hmm.covars_=covars
########���ϣ�������ѵ��������HMMģ�ͣ�����û��ѵ��ֱ�Ӹ�����������Ҫѵ����fit��
#�۲�״̬��ά��ʹ����ά�۲����У�����3*2*2����
seen = np.array([[1.1,2.0],[-1,2.0],[3,7]])
logprob, state = hmm.decode(seen, algorithm="viterbi")
print(state)
#HMM����1�������ʼ���
print(hmm.score(seen))
