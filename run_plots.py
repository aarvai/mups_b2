mups_ELBI('2013:215:15:49:00', '2013:215:15:54:00')
mups_ELBI('2013:231:11:25:00', '2013:231:12:00:00')

#mups_delta_ELBI('2013:215:15:49:00', '2013:215:15:54:00') #not particularly helpful
#mups_delta_ELBI('2013:231:11:25:00', '2013:231:12:00:00') #not particularly helpful

mups_2_temps('2013:215:12:00:00', '2013:215:18:30:00')
mups_2_temps('2013:231:09:00:00', '2013:231:14:00:00')

#mups_2_delta_temps('2013:215:15:35:00', '2013:215:16:43:00') #2A dropped out
mups_2_delta_temps('2013:231:10:35:00', '2013:231:12:45:00')

mups_2_temps_xout_2()

timeline('2013:215:12:00:00', '2013:215:18:30:00')  
timeline('2013:231:09:00:00', '2013:231:14:00:00') 

# Individual Firings for Checkout #1
mups_ELBI('2013:215:15:49:11', '2013:215:15:50:11', savefig='2013_215_elbi_01_1b.png')  # MUPS-2B 
mups_ELBI('2013:215:15:50:23', '2013:215:15:51:23', savefig='2013_215_elbi_02_3b.png')  # MUPS-1B
mups_ELBI('2013:215:15:51:35', '2013:215:15:52:35', savefig='2013_215_elbi_03_2b.png')  # MUPS-2B 
mups_ELBI('2013:215:15:52:46', '2013:215:15:53:46', savefig='2013_215_elbi_04_4b.png')  # MUPS-2B 

# Individual Firings for Checkout #2
mups_ELBI('2013:231:11:26:06', '2013:231:11:27:06', savefig='2013_231_elbi_01_2b.png')  # MUPS-2B try 1
mups_ELBI('2013:231:11:27:54', '2013:231:11:28:54', savefig='2013_231_elbi_02_1b.png')  # MUPS-1B
mups_ELBI('2013:231:11:30:42', '2013:231:11:31:42', savefig='2013_231_elbi_03_2b.png')  # MUPS-2B try 2
mups_ELBI('2013:231:11:31:50', '2013:231:11:32:50', savefig='2013_231_elbi_04_2b.png')  # MUPS-2B try 3
mups_ELBI('2013:231:11:33:07', '2013:231:11:34:07', savefig='2013_231_elbi_05_2b.png')  # MUPS-2B try 4
mups_ELBI('2013:231:11:34:15', '2013:231:11:35:15', savefig='2013_231_elbi_06_2b.png')  # MUPS-2B try 5
mups_ELBI('2013:231:11:37:00', '2013:231:11:38:00', savefig='2013_231_elbi_07_1b.png')  # MUPS-1B
mups_ELBI('2013:231:11:38:30', '2013:231:11:39:30', savefig='2013_231_elbi_08_3b.png')  # MUPS-3B 
mups_ELBI('2013:231:11:41:12', '2013:231:11:42:12', savefig='2013_231_elbi_09_4b.png')  # MUPS-4B
mups_ELBI('2013:231:11:44:00', '2013:231:11:45:00', savefig='2013_231_elbi_10_2b.png')  # MUPS-2B try 6
mups_ELBI('2013:231:11:45:12', '2013:231:11:46:12', savefig='2013_231_elbi_11_2b.png')  # MUPS-2B try 7
mups_ELBI('2013:231:11:46:22', '2013:231:11:47:22', savefig='2013_231_elbi_12_2b.png')  # MUPS-2B try 8
mups_ELBI('2013:231:11:51:34', '2013:231:11:52:34', savefig='2013_231_elbi_13_2b.png')  # MUPS-2B try 9
mups_ELBI('2013:231:11:56:54', '2013:231:11:57:54', savefig='2013_231_elbi_14_2b.png')  # MUPS-2B try 10