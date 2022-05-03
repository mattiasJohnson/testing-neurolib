from numpy import array as array

params_multimodel = {'ALNThlmNet.ALNNode_0.ALNMassEXC_0.Ke': 800.0,
 'ALNThlmNet.ALNNode_0.ALNMassEXC_0.Ki': 200.0,
 'ALNThlmNet.ALNNode_0.ALNMassEXC_0.c_gl': 0.4,
 'ALNThlmNet.ALNNode_0.ALNMassEXC_0.Ke_gl': 250.0,
 'ALNThlmNet.ALNNode_0.ALNMassEXC_0.tau_se': 2.0,
 'ALNThlmNet.ALNNode_0.ALNMassEXC_0.tau_si': 5.0,
 'ALNThlmNet.ALNNode_0.ALNMassEXC_0.sigmae_ext': 1.5,
 'ALNThlmNet.ALNNode_0.ALNMassEXC_0.Jee_max': 2.43,
 'ALNThlmNet.ALNNode_0.ALNMassEXC_0.Jei_max': -3.3,
 'ALNThlmNet.ALNNode_0.ALNMassEXC_0.C': 200.0,
 'ALNThlmNet.ALNNode_0.ALNMassEXC_0.gL': 10.0,
 'ALNThlmNet.ALNNode_0.ALNMassEXC_0.ext_exc_current': 0.0,
 'ALNThlmNet.ALNNode_0.ALNMassEXC_0.ext_exc_rate': 0.0,
 'ALNThlmNet.ALNNode_0.ALNMassEXC_0.a': 0.0,
 'ALNThlmNet.ALNNode_0.ALNMassEXC_0.b': 15.0,
 'ALNThlmNet.ALNNode_0.ALNMassEXC_0.EA': -80.0,
 'ALNThlmNet.ALNNode_0.ALNMassEXC_0.tauA': 1000.0,
 'ALNThlmNet.ALNNode_0.ALNMassEXC_0.lambda': 10.0,
 'ALNThlmNet.ALNNode_0.ALNMassEXC_0.input_0.type': 'OrnsteinUhlenbeckProcess',
 'ALNThlmNet.ALNNode_0.ALNMassEXC_0.input_0.mu': 3.05,
 'ALNThlmNet.ALNNode_0.ALNMassEXC_0.input_0.sigma': 0.05,
 'ALNThlmNet.ALNNode_0.ALNMassEXC_0.input_0.tau': 5.0,
 'ALNThlmNet.ALNNode_0.ALNMassEXC_0.input_0.n': 1,
 'ALNThlmNet.ALNNode_0.ALNMassEXC_0.input_0.seed': 40,
 'ALNThlmNet.ALNNode_0.ALNMassINH_1.Ke': 800.0,
 'ALNThlmNet.ALNNode_0.ALNMassINH_1.Ki': 200.0,
 'ALNThlmNet.ALNNode_0.ALNMassINH_1.c_gl': 0.4,
 'ALNThlmNet.ALNNode_0.ALNMassINH_1.Ke_gl': 250.0,
 'ALNThlmNet.ALNNode_0.ALNMassINH_1.tau_se': 2.0,
 'ALNThlmNet.ALNNode_0.ALNMassINH_1.tau_si': 5.0,
 'ALNThlmNet.ALNNode_0.ALNMassINH_1.sigmai_ext': 1.5,
 'ALNThlmNet.ALNNode_0.ALNMassINH_1.Jie_max': 2.6,
 'ALNThlmNet.ALNNode_0.ALNMassINH_1.Jii_max': -1.64,
 'ALNThlmNet.ALNNode_0.ALNMassINH_1.C': 200.0,
 'ALNThlmNet.ALNNode_0.ALNMassINH_1.gL': 10.0,
 'ALNThlmNet.ALNNode_0.ALNMassINH_1.ext_inh_current': 0.0,
 'ALNThlmNet.ALNNode_0.ALNMassINH_1.ext_inh_rate': 0.0,
 'ALNThlmNet.ALNNode_0.ALNMassINH_1.lambda': 10.0,
 'ALNThlmNet.ALNNode_0.ALNMassINH_1.input_0.type': 'OrnsteinUhlenbeckProcess',
 'ALNThlmNet.ALNNode_0.ALNMassINH_1.input_0.mu': 2.0,
 'ALNThlmNet.ALNNode_0.ALNMassINH_1.input_0.sigma': 0.05,
 'ALNThlmNet.ALNNode_0.ALNMassINH_1.input_0.tau': 5.0,
 'ALNThlmNet.ALNNode_0.ALNMassINH_1.input_0.n': 1,
 'ALNThlmNet.ALNNode_0.ALNMassINH_1.input_0.seed': 40,
 'ALNThlmNet.ALNNode_0.local_connectivity': array([[0.24691358, 0.75757576],
        [0.23076923, 1.52439024]]),
 'ALNThlmNet.ALNNode_0.local_delays': array([[4., 2.],
        [4., 2.]]),
 'ALNThlmNet.THLMnode_1.TCR_0.tau': 20.0,
 'ALNThlmNet.THLMnode_1.TCR_0.Q_max': 0.4,
 'ALNThlmNet.THLMnode_1.TCR_0.theta': -58.5,
 'ALNThlmNet.THLMnode_1.TCR_0.sigma': 6.0,
 'ALNThlmNet.THLMnode_1.TCR_0.C1': 1.8137993642,
 'ALNThlmNet.THLMnode_1.TCR_0.C_m': 1.0,
 'ALNThlmNet.THLMnode_1.TCR_0.gamma_e': 0.07,
 'ALNThlmNet.THLMnode_1.TCR_0.gamma_r': 0.1,
 'ALNThlmNet.THLMnode_1.TCR_0.g_L': 1.0,
 'ALNThlmNet.THLMnode_1.TCR_0.g_GABA': 1.0,
 'ALNThlmNet.THLMnode_1.TCR_0.g_AMPA': 1.0,
 'ALNThlmNet.THLMnode_1.TCR_0.g_LK': 0.032,
 'ALNThlmNet.THLMnode_1.TCR_0.g_T': 3.0,
 'ALNThlmNet.THLMnode_1.TCR_0.g_h': 0.062,
 'ALNThlmNet.THLMnode_1.TCR_0.E_AMPA': 0.0,
 'ALNThlmNet.THLMnode_1.TCR_0.E_GABA': -70.0,
 'ALNThlmNet.THLMnode_1.TCR_0.E_L': -70.0,
 'ALNThlmNet.THLMnode_1.TCR_0.E_K': -100.0,
 'ALNThlmNet.THLMnode_1.TCR_0.E_Ca': 120.0,
 'ALNThlmNet.THLMnode_1.TCR_0.E_h': -40.0,
 'ALNThlmNet.THLMnode_1.TCR_0.alpha_Ca': -5.18e-05,
 'ALNThlmNet.THLMnode_1.TCR_0.tau_Ca': 10.0,
 'ALNThlmNet.THLMnode_1.TCR_0.Ca_0': 0.00024,
 'ALNThlmNet.THLMnode_1.TCR_0.k1': 25000000.0,
 'ALNThlmNet.THLMnode_1.TCR_0.k2': 0.0004,
 'ALNThlmNet.THLMnode_1.TCR_0.k3': 0.1,
 'ALNThlmNet.THLMnode_1.TCR_0.k4': 0.001,
 'ALNThlmNet.THLMnode_1.TCR_0.n_P': 4.0,
 'ALNThlmNet.THLMnode_1.TCR_0.g_inc': 2.0,
 'ALNThlmNet.THLMnode_1.TCR_0.ext_current': 0.0,
 'ALNThlmNet.THLMnode_1.TCR_0.lambda': 10.0,
 'ALNThlmNet.THLMnode_1.TCR_0.input_0.type': 'OrnsteinUhlenbeckProcess',
 'ALNThlmNet.THLMnode_1.TCR_0.input_0.mu': 0.0,
 'ALNThlmNet.THLMnode_1.TCR_0.input_0.sigma': 0.005,
 'ALNThlmNet.THLMnode_1.TCR_0.input_0.tau': 5.0,
 'ALNThlmNet.THLMnode_1.TCR_0.input_0.n': 1,
 'ALNThlmNet.THLMnode_1.TCR_0.input_0.seed': 40,
 'ALNThlmNet.THLMnode_1.TRN_1.tau': 20.0,
 'ALNThlmNet.THLMnode_1.TRN_1.Q_max': 0.4,
 'ALNThlmNet.THLMnode_1.TRN_1.theta': -58.5,
 'ALNThlmNet.THLMnode_1.TRN_1.sigma': 6.0,
 'ALNThlmNet.THLMnode_1.TRN_1.C1': 1.8137993642,
 'ALNThlmNet.THLMnode_1.TRN_1.C_m': 1.0,
 'ALNThlmNet.THLMnode_1.TRN_1.gamma_e': 0.07,
 'ALNThlmNet.THLMnode_1.TRN_1.gamma_r': 0.1,
 'ALNThlmNet.THLMnode_1.TRN_1.g_L': 1.0,
 'ALNThlmNet.THLMnode_1.TRN_1.g_GABA': 1.0,
 'ALNThlmNet.THLMnode_1.TRN_1.g_AMPA': 1.0,
 'ALNThlmNet.THLMnode_1.TRN_1.g_LK': 0.032,
 'ALNThlmNet.THLMnode_1.TRN_1.g_T': 2.3,
 'ALNThlmNet.THLMnode_1.TRN_1.E_AMPA': 0.0,
 'ALNThlmNet.THLMnode_1.TRN_1.E_GABA': -70.0,
 'ALNThlmNet.THLMnode_1.TRN_1.E_L': -70.0,
 'ALNThlmNet.THLMnode_1.TRN_1.E_K': -100.0,
 'ALNThlmNet.THLMnode_1.TRN_1.E_Ca': 120.0,
 'ALNThlmNet.THLMnode_1.TRN_1.ext_current': 0.0,
 'ALNThlmNet.THLMnode_1.TRN_1.lambda': 10.0,
 'ALNThlmNet.THLMnode_1.TRN_1.input_0.type': 'ZeroInput',
 'ALNThlmNet.THLMnode_1.TRN_1.input_0.n': 1,
 'ALNThlmNet.THLMnode_1.TRN_1.input_0.seed': 40,
 'ALNThlmNet.THLMnode_1.local_connectivity': array([[ 0.,  5.],
        [ 3., 25.]]),
 'ALNThlmNet.THLMnode_1.local_delays': array([[0., 0.],
        [0., 0.]]),
 'ALNThlmNet.connectivity': array([[0.  , 0.12],
        [1.2 , 0.  ]]),
 'ALNThlmNet.delays': array([[ 0., 13.],
        [13.,  0.]]),
 'duration': 360000,
 'dt': 0.01,
 'seed': 40,
 'backend': 'numba',
 'name': 'ALNThlmNet',
 'description': 'ALN 1 node + Thalamus',
 'N': 2,
 'Cmat': array([[0.  , 0.12],
        [1.2 , 0.  ]]),
 'sampling_dt': 1.0}




params_connected_imported = {

# CORTEX
# --- Cortex exc ---
 'Ke': 800.0,  # same
 'Ki': 200.0,  # same
 'c_gl': 0.4,  # 0.3 in native
 'Ke_gl': 250.0,  # same
 'tau_se': 2.0,  # same
 'tau_si': 5.0,  # same
 'sigmae_ext': 1.5,  # same
 'Jee_max': 2.43,  # same
 'Jei_max': -3.3,  # same
 'C': 200.0,  # same
 'gL': 10.0,  # same
 'ext_exc_current': 0.0,  # same
 'ext_exc_rate': 0.0,  # same
 'a': 0.0,  # same
 'b': 15.0,  # 0 in native
 'EA': -80.0,  # same
 'tauA': 1000.0,  # 200 in native
 'lambda': 10.0,  # ??
# 'input_0.type': 'OrnsteinUhlenbeckProcess',  # defines exc ALN
# 'input_0.mu': 3.05,  # assume called  mue_ext_mean
# 'input_0.sigma': 0.05,
# 'input_0.tau': 5.0,
# 'input_0.n': 1,
# 'input_0.seed': 40,
 'mue_ext_mean': 3.05,
 'sigma_ou': 0.05,  # 0 in native
 'tau_ou': 5,  
# --- Cortex inh ---
# 'Ke': 800.0,
# 'Ki': 200.0,
# 'c_gl': 0.4,
# 'Ke_gl': 250.0,
# 'tau_se': 2.0,
# 'tau_si': 5.0,
 'sigmai_ext': 1.5,  # same
 'Jie_max': 2.6,  # same
 'Jii_max': -1.64,  # same
# 'C': 200.0,
# 'gL': 10.0,
 'ext_inh_current': 0.0,  # same
 'ext_inh_rate': 0.0,  # same
 'lambda': 10.0,  # ??
# 'input_0.type': 'OrnsteinUhlenbeckProcess',  # defines inh ALN
# 'input_0.mu': 2.0,  # assume called mui_ext_mean
# 'input_0.sigma': 0.05,
# 'input_0.tau': 5.0,
# 'input_0.n': 1,
# 'input_0.seed': 40,
  'mui_ext_mean': 2.0,
# 'ALNThlmNet.ALNNode_0.local_connectivity': array([[0.24691358, 0.75757576],  # assumes defines cee, cie ...
#        [0.23076923, 1.52439024]]),
#'ALNThlmNet.ALNNode_0.local_delays': array([[4., 2.],  # de di
#        [4., 2.]]),
 # THALAMUS
 # THalamocortical (TCR)
 'tau': 20.0,  # same
 'Q_max': 0.4,  # same
 'theta': -58.5,  # same
 'sigma': 6.0,  # same
 'C1': 1.8137993642,  # same
 'C_m': 1.0,  # same
 'gamma_e': 0.07,  # same
 'gamma_r': 0.1,  # same
 'g_L': 1.0,  # same
 'g_GABA': 1.0,  # same
 'g_AMPA': 1.0,  # same
 'g_LK': 0.032,  # was 0.018 in thalamus native
 'g_T_t': 3.0,  # called g_T in multimodel
 'g_h': 0.062,  # same
 'E_AMPA': 0.0,  # same
 'E_GABA': -70.0,  # same
 'E_L': -70.0,  # same
 'E_K': -100.0,  # same
 'E_Ca': 120.0,  # same
 'E_h': -40.0,  # same
 'alpha_Ca': -5.18e-05,  # same
 'tau_Ca': 10.0,  # same
 'Ca_0': 0.00024,  # same
 'k1': 25000000.0,  # same
 'k2': 0.0004,  # same
 'k3': 0.1,  # same
 'k4': 0.001,  #same
 'n_P': 4.0,  # same
 'g_inc': 2.0,  # same
 'ext_current_t': 0.0,  # called ext_current in multimodel
 'lambda': 10.0,  # ?? Can't find in native
# 'input_0.type': 'OrnsteinUhlenbeckProcess',  # ? maybe called noise
# 'input_0.mu': 0.0,
# 'input_0.sigma': 0.005,
# 'input_0.tau': 5.0,
# 'input_0.n': 1,
# 'input_0.seed': 40,
# 'mue_ext_mean': 0, DOES NOT EXIST IN THALAMUS NATIVE MODEL
 # RETICULAR (TRN)
 'tau': 20.0,  # same
 'Q_max': 0.4,  # same
 'theta': -58.5,  # same
 'sigma': 6.0,  # same
 'C1': 1.8137993642,  # same
 'C_m': 1.0,  # same
 'gamma_e': 0.07,  # same
 'gamma_r': 0.1,  # same
 'g_L': 1.0,  # same
 'g_GABA': 1.0,  # same
 'g_AMPA': 1.0,  # same
 'g_LK': 0.032,  # was 0.018 in thalamus native
 'g_T_r': 2.3,  # called g_T in multimodel
 'E_AMPA': 0.0,  # same
 'E_GABA': -70.0,  # same
 'E_L': -70.0,  # same
 'E_K': -100.0,  # same
 'E_Ca': 120.0,  # same
 'ext_current_r': 0.0,  # called ext_current in multimodel
 'lambda': 10.0,  # ??
# 'input_0.type': 'ZeroInput',
# 'input_0.n': 1,
# 'input_0.seed': 40,
    'N_tr': 5,
    'N_rt': 3,
    'N_rr': 25,
 # 'ALNThlmNet.THLMnode_1.local_connectivity': array([[ 0.,  5.],  # Defines N_tt|tr|rt|rr
        # [ 3., 25.]]),
 # 'ALNThlmNet.THLMnode_1.local_delays': array([[0., 0.],
        # [0., 0.]]),
 # ' ALNThlmNet.connectivity': array([[0.  , 0.12], # same as Cmat which is also present in multimodel??
 #        [1.2 , 0.  ]]),
# 'ALNThlmNet.delays': array([[ 0., 13.],  # called lengthMat in native
#        [13.,  0.]]),
 'duration': 4000,  # 360000 in multimodel, lowered for testing
 'dt': 0.01,  # same
#  'seed': 40,
#  'backend': 'numba',
#  'name': 'ALNThlmNet',
#  'description': 'ALN 1 node + Thalamus',
#  'N': 2,
 'Cmat': array([[0.  , 0.12],
        [1.2 , 0.  ]]),
 'sampling_dt': 1.0, # ??
# --- NEW NAMING ---
  'lengthMat': array([[ 0., 13*20],
        [13*20,  0.]]),
  'cee': 0.24691358,  # Assume from local_connections ALN
  'cie': 0.23076923,
  'cei': 0.75757576,
  'cii': 1.52439024,
  'de': 4,  # From local_delays ALN
  'di': 2,
# --- MISSING ---
  'n_nodes_ctx': 1,
  'n_nodes_thal': 1,
   'n_nodes_tot': 2,
  'seed': 42,
 
}  