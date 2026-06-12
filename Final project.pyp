<?xml version='1.0' encoding='utf-8'?>
<scheme version="2.0" title="Final project" description="">
	<bookmarks>
		<bookmark x="null" y="null" />
		<bookmark x="null" y="null" />
		<bookmark x="null" y="null" />
		<bookmark x="null" y="null" />
		<bookmark x="null" y="null" />
		<bookmark x="null" y="null" />
		<bookmark x="null" y="null" />
		<bookmark x="null" y="null" />
		<bookmark x="null" y="null" />
		<bookmark x="null" y="null" />
	</bookmarks>
	<nodes>
		<node id="0" name="Import SET" qualified_name="widgets.file_system.owimportset.OWImportSET" project_name="NeuroPype" version="1.2.3" title="Import SET&#10;[/Users/cyc/Desktop/HIP_final/sub-12_task-oddball_eeg_final.set]" uuid="479b0c06-9a41-43f5-8e90-be9907acbe2c" position="(141.25, 255.0)" />
		<node id="1" name="Re-referencing" qualified_name="widgets.signal_processing.owrereferencing.OWRereferencing" project_name="NeuroPype" version="1.1.0" title="Re-referencing&#10;[: along space]" uuid="aaf9be96-880d-4df7-b4e9-41026d1f1770" position="(375.7954545454546, 246.25)" />
		<node id="2" name="IIR Filter" qualified_name="widgets.signal_processing.owiirfilter.OWIIRFilter" project_name="NeuroPype" version="1.1.0" title="IIR Filter&#10;[[0.1, 0.5, 45, 50]Hz bandpass -45dB butter]" uuid="02bf5909-c2b3-463c-ba4b-2f52a0e3a2bb" position="(496.93181818181824, 253.75)" />
		<node id="3" name="Artifact Removal" qualified_name="widgets.neural.owartifactremoval.OWArtifactRemoval" project_name="NeuroPype" version="2.4.1" title="Artifact Removal&#10;[cutoff:7.5]" uuid="dcdc1ff9-2fb9-4735-b0b6-6dc419c3a78e" position="(612.0454545454545, 245.0)" />
		<node id="4" name="Time Series Plot" qualified_name="widgets.visualization.owtimeseriesplot.OWTimeSeriesPlot" project_name="NeuroPype" version="1.2.3" title="Time Series Plot&#10;[time x space]" uuid="19d82864-c14e-4b17-9df6-f83e3f3b0f24" position="(930.6818181818185, 246.1363636363635)" />
		<node id="5" name="Dejitter Timestamps" qualified_name="widgets.utilities.owdejittertimestamps.OWDejitterTimestamps" project_name="NeuroPype" version="1.0.0" title="Dejitter Timestamps" uuid="adafb869-5058-4379-a767-4c13b771f46a" position="(260.68181818181824, 255.0000000000001)" />
		<node id="6" name="Segmentation" qualified_name="widgets.formatting.owsegmentation.OWSegmentation" project_name="NeuroPype" version="1.0.4" title="Segmentation&#10;[[-3, 3]]" uuid="2450586b-fd0f-40c7-943b-69f79adb647d" position="(717.954545454545, 245.79545454545462)" />
		<node id="7" name="Mean" qualified_name="widgets.statistics.owmean.OWMean" project_name="NeuroPype" version="1.1.0" title="Mean&#10;[over instance (retained)]" uuid="f5076463-574c-4088-8b33-8ce9bac3c7e0" position="(820.2272727272725, 245.68181818181813)" />
		<node id="8" name="Power Spectrum (Welch)" qualified_name="widgets.spectral.owwelchspectrum.OWWelchSpectrum" project_name="NeuroPype" version="1.3.1" title="Power Spectrum (Welch)&#10;[whole window samples, overlap:50%, density]" uuid="ada4d230-b48b-46b3-b7c5-52e86f065e63" position="(618.75, 387.5)" />
		<node id="9" name="Spectrum Plot" qualified_name="widgets.visualization.owspectrumplot.OWSpectrumPlot" project_name="NeuroPype" version="2.1.0" title="Spectrum Plot&#10;[dB x:None y:[-380, 100]not-stacked]" uuid="169d02f0-e2ba-44cd-b301-537309be4bdd" position="(727.5, 387.5)" />
		<node id="10" name="Power Spectrum (Welch)" qualified_name="widgets.spectral.owwelchspectrum.OWWelchSpectrum" project_name="NeuroPype" version="1.3.1" title="Power Spectrum (Welch)&#10;[whole window samples, overlap:50%, density]" uuid="dea0f0b6-dc1c-434c-b2a4-6b8a960f437c" position="(498.125, 87.5)" />
		<node id="11" name="Spectrum Plot" qualified_name="widgets.visualization.owspectrumplot.OWSpectrumPlot" project_name="NeuroPype" version="2.1.0" title="Spectrum Plot&#10;[dB x:None y:[-100, 100]not-stacked]" uuid="e932a08a-f6aa-483e-90b5-4d6f9977a046" position="(606.875, 87.5)" />
		<node id="12" name="Export Markers to CSV" qualified_name="widgets.markers.owexportmarkers.OWExportMarkers" project_name="NeuroPype" version="1.1.1" title="Export Markers to CSV" uuid="5eeda6c5-f85c-4a90-8fb9-4a8a11755ccc" position="(370.0, 375.0)" />
	</nodes>
	<links>
		<link id="0" source_node_id="1" sink_node_id="2" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="1" source_node_id="2" sink_node_id="3" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="2" source_node_id="5" sink_node_id="1" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="3" source_node_id="6" sink_node_id="7" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="4" source_node_id="7" sink_node_id="4" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="5" source_node_id="0" sink_node_id="5" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="6" source_node_id="3" sink_node_id="6" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="7" source_node_id="2" sink_node_id="8" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="8" source_node_id="8" sink_node_id="9" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="9" source_node_id="10" sink_node_id="11" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="10" source_node_id="1" sink_node_id="10" source_channel="Data" sink_channel="Data" enabled="true" />
		<link id="11" source_node_id="5" sink_node_id="12" source_channel="Data" sink_channel="Data" enabled="true" />
	</links>
	<annotations />
	<thumbnail />
	<node_properties>
		<properties node_id="0" format="pickle">gASVagEAAAAAAAB9lCiMDWNsb3VkX2FjY291bnSUjA0odXNlIGRlZmF1bHQplIwMY2xvdWRfYnVj
a2V0lGgCjBFjbG91ZF9jcmVkZW50aWFsc5RoAowKY2xvdWRfaG9zdJSMB0RlZmF1bHSUjAhmaWxl
bmFtZZSMPi9Vc2Vycy9jeWMvRGVza3RvcC9ISVBfZmluYWwvc3ViLTEyX3Rhc2stb2RkYmFsbF9l
ZWdfZmluYWwuc2V0lIwIbWV0YWRhdGGUfZSME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjAlQeVF0Ni5z
aXCUjA5fdW5waWNrbGVfdHlwZZSTlIwMUHlRdDYuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsA
AwAAAAACEgAAAMQAAAN5AAACXwAAAhIAAADgAAADeQAAAl8AAAAAAAAAAAWgAAACEgAAAOAAAAN5
AAACX5SFlIeUUpSMDnNldF9icmVha3BvaW50lIl1Lg==
</properties>
		<properties node_id="1" format="pickle">gASVWAEAAAAAAAB9lCiMBGF4aXOUjAVzcGFjZZSMCGN1dF9wcm9wlEc/uZmZmZmZmowJZXN0aW1h
dG9ylIwEbWVhbpSMC2lnbm9yZV9uYW5zlImMCG1ldGFkYXRhlH2UjA9yZWZlcmVuY2VfcmFuZ2WU
jAE6lIwOcmVmZXJlbmNlX3VuaXSUjARhdXRvlIwTc2F2ZWRXaWRnZXRHZW9tZXRyeZSMCVB5UXQ2
LnNpcJSMDl91bnBpY2tsZV90eXBllJOUjAxQeVF0Ni5RdENvcmWUjApRQnl0ZUFycmF5lENCAdnQ
ywADAAAAAAN7AAAAowAABPkAAAKgAAADewAAAL8AAAT5AAACoAAAAAAAAAAABaAAAAN7AAAAvwAA
BPkAAAKglIWUh5RSlIwOc2V0X2JyZWFrcG9pbnSUiYwWdXNlX3NlcGFyYXRlX3JlZmVyZW5jZZSJ
jAd2ZXJib3NllIh1Lg==
</properties>
		<properties node_id="2" format="pickle">gASVgAEAAAAAAAB9lCiMBGF4aXOUjAR0aW1llIwGZGVzaWdulIwGYnV0dGVylIwLZnJlcXVlbmNp
ZXOUXZQoRz+5mZmZmZmaRz/gAAAAAAAASy1LMmWMC2lnbm9yZV9uYW5zlImMCG1ldGFkYXRhlH2U
jARtb2RllIwIYmFuZHBhc3OUjBBvZmZsaW5lX2ZpbHRmaWx0lImMBW9yZGVylIwNKHVzZSBkZWZh
dWx0KZSMCXBhc3NfbG9zc5RHP+AAAAAAAACME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjAlQeVF0Ni5z
aXCUjA5fdW5waWNrbGVfdHlwZZSTlIwMUHlRdDYuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsA
AwAAAAACEgAAAEwAAAN5AAAC2AAAAhIAAABoAAADeQAAAtgAAAAAAAAAAAWgAAACEgAAAGgAAAN5
AAAC2JSFlIeUUpSMDnNldF9icmVha3BvaW50lImMCnN0b3BfYXR0ZW6UR0BGgAAAAAAAdS4=
</properties>
		<properties node_id="3" format="pickle">gASV0gIAAAAAAAB9lCiMAWGUjA0odXNlIGRlZmF1bHQplIwBYpRoAowKYmxvY2tfc2l6ZZRoAowN
Y2FsaWJfc2Vjb25kc5RLLYwGY3V0b2ZmlEdAHgAAAAAAAIwPZW1pdF9jYWxpYl9kYXRhlIiMB2lu
aXRfb26UXZSMCWxvb2thaGVhZJRoAowQbWF4X2JhZF9jaGFubmVsc5RHP8mZmZmZmZqMCG1heF9k
aW1zlEcAAAAAAAAAAIwUbWF4X2Ryb3BvdXRfZnJhY3Rpb26URz+5mZmZmZmajAdtYXhfbWVtlE0A
AYwIbWV0YWRhdGGUfZSMEm1pbl9jbGVhbl9mcmFjdGlvbpRHP9AAAAAAAACMFW1pbl9yZXF1aXJl
ZF9jaGFubmVsc5RLAowNcHJlc2VydmVfYmFuZJRoAowKcmllbWFubmlhbpSJjBNzYXZlZFdpZGdl
dEdlb21ldHJ5lIwJUHlRdDYuc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ2LlF0Q29yZZSM
ClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAAAgoAAAA4AAADgQAAAukAAAIKAAAAVAAAA4EAAALpAAAA
AAAAAAAFoAAAAgoAAABUAAADgQAAAumUhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJjA1zdGRkZXZf
Y3V0b2ZmlEsUjAlzdGVwX3NpemWURz/JmZmZmZmajBB1c2VfY2xlYW5fd2luZG93lIiMCnVzZV9s
ZWdhY3mUiYwWd2luZG93X2xlbl9jbGVhbndpbmRvd5RHP+AAAAAAAACMDXdpbmRvd19sZW5ndGiU
Rz/gAAAAAAAAjA53aW5kb3dfb3ZlcmxhcJRHP+UeuFHrhR+MGndpbmRvd19vdmVybGFwX2NsZWFu
d2luZG93lEc/5R64UeuFH4wRenNjb3JlX3RocmVzaG9sZHOUXZQoSvv///9LB2V1Lg==
</properties>
		<properties node_id="4" format="pickle">gASVmAMAAAAAAAB9lCiMDWFic29sdXRlX3RpbWWUiIwNYWx3YXlzX29uX3RvcJSJjBRhbm5vdGF0
aW9uX2ZvbnRfc2l6ZZRHQCYAAAAAAACMC2FudGlhbGlhc2VklIiMEGF1dG9fbGluZV9jb2xvcnOU
iIwJYXV0b3NjYWxllIiMEGJhY2tncm91bmRfY29sb3KUjAcjMzAzMDMwlIwIY29sb3JtYXCUjAxn
aXN0X3JhaW5ib3eUjBBkZWNvcmF0aW9uX2NvbG9ylIwHI0IwQjBCMJSMCWZvbnRfc2l6ZZRHQCYA
AAAAAACMDGluaXRpYWxfZGltc5RdlChLMksyTegDTSADZYwObGFiZWxfcm90YXRpb26UjApob3Jp
em9udGFslIwLbGVmdF9vZmZzZXSUSwCMCmxpbmVfY29sb3KUjAV3aGl0ZZSMCmxpbmVfd2lkdGiU
Rz/0AAAAAAAAjAxtYXJrZXJfY29sb3KUjApkYXJrb3JhbmdllIwMbWF4X2NoYW5uZWxzlEsjjAht
ZXRhZGF0YZR9lIwMbmFuc19hc196ZXJvlImMDm5vX2NvbmNhdGVuYXRllImMDm92ZXJyaWRlX3Ny
YXRllIwNKHVzZSBkZWZhdWx0KZSMDHBsb3RfbWFya2Vyc5SJjAtwbG90X21pbm1heJSJjBNzYXZl
ZFdpZGdldEdlb21ldHJ5lIwJUHlRdDYuc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ2LlF0
Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAAAhEAAAA6AAADeAAAAusAAAIRAAAAVgAAA3gA
AALrAAAAAAAAAAAFoAAAAhEAAABWAAADeAAAAuuUhZSHlFKUjAVzY2FsZZRHP/AAAAAAAACMDnNl
dF9icmVha3BvaW50lImMDHNob3dfdG9vbGJhcpSJjAZzdHJlYW2UaB6MC3N0cmVhbV9uYW1llGge
jAx0aWdodF9sYXlvdXSUiIwKdGltZV9yYW5nZZRHQBgAAAAAAACMBXRpdGxllIwLVGltZSBTZXJp
ZXOUjBV0cmFja193aW5kb3dfcG9zaXRpb26UiYwHdmVyYm9zZZSJjAZ4X2F4aXOUjAR0aW1llIwH
eF9sYWJlbJRoHowGeV9heGlzlIwFc3BhY2WUjAd5X2xhYmVslGgejAp6ZXJvX2NvbG9ylIwHIzYw
NjA2MJSMCHplcm9tZWFulIh1Lg==
</properties>
		<properties node_id="5" format="pickle">gASVGAEAAAAAAAB9lCiMD2ZvcmNlX21vbm90b25pY5SIjA9mb3JnZXRfaGFsZnRpbWWUR0BWgAAA
AAAAjA5tYXhfdXBkYXRlcmF0ZZRN6AOMCG1ldGFkYXRhlH2UjBNzYXZlZFdpZGdldEdlb21ldHJ5
lIwJUHlRdDYuc2lwlIwOX3VucGlja2xlX3R5cGWUk5SMDFB5UXQ2LlF0Q29yZZSMClFCeXRlQXJy
YXmUQ0IB2dDLAAMAAAAAAhIAAADoAAADeQAAAkgAAAISAAABBAAAA3kAAAJIAAAAAAAAAAAFoAAA
AhIAAAEEAAADeQAAAkiUhZSHlFKUjA5zZXRfYnJlYWtwb2ludJSJjA53YXJtdXBfc2FtcGxlc5RK
/////3Uu
</properties>
		<properties node_id="6" format="pickle">gASVaAEAAAAAAAB9lCiMEWtlZXBfbWFya2VyX2NodW5rlImMDm1heF9nYXBfbGVuZ3RolEc/yZmZ
mZmZmowIbWV0YWRhdGGUfZSMD29ubGluZV9lcG9jaGluZ5SMDW1hcmtlci1sb2NrZWSUjA1zYW1w
bGVfb2Zmc2V0lEsAjBNzYXZlZFdpZGdldEdlb21ldHJ5lIwJUHlRdDYuc2lwlIwOX3VucGlja2xl
X3R5cGWUk5SMDFB5UXQ2LlF0Q29yZZSMClFCeXRlQXJyYXmUQ0IB2dDLAAMAAAAAAhIAAACIAAAD
eQAAArsAAAISAAAApAAAA3kAAAK7AAAAAAAAAAAFoAAAAhIAAACkAAADeQAAAruUhZSHlFKUjA5z
ZWxlY3RfbWFya2Vyc5SMDSh1c2UgZGVmYXVsdCmUjA5zZXRfYnJlYWtwb2ludJSJjAt0aW1lX2Jv
dW5kc5RdlChK/f///0sDZYwHdmVyYm9zZZSJdS4=
</properties>
		<properties node_id="7" format="pickle">gASVtwEAAAAAAAB9lCiMBGF4aXOUjAhpbnN0YW5jZZSMD2F4aXNfb2NjdXJyZW5jZZRLAIwHYmFj
a2VuZJSMBGtlZXCUjBJmb3JjZV9mZWF0dXJlX2F4aXOUjA0odXNlIGRlZmF1bHQplIwLaWdub3Jl
X25hbnOUiYwJa2VlcF9heGlzlIiMCWtlcHRfYXhpc5SMBmxlZ2FjeZSMCG1ldGFkYXRhlH2UjAlw
cmVjaXNpb26UjARrZWVwlIwNcmVjdXJzZV9saXN0c5SJjAZyb2J1c3SUiYwVcm9idXN0X2VzdGlt
YXRvcl90eXBllIwGbWVkaWFulIwTc2F2ZWRXaWRnZXRHZW9tZXRyeZSMCVB5UXQ2LnNpcJSMDl91
bnBpY2tsZV90eXBllJOUjAxQeVF0Ni5RdENvcmWUjApRQnl0ZUFycmF5lENCAdnQywADAAAAAAIS
AAAAOgAAA3kAAALrAAACEgAAAFYAAAN5AAAC6wAAAAAAAAAABaAAAAISAAAAVgAAA3kAAALrlIWU
h5RSlIwOc2V0X2JyZWFrcG9pbnSUiYwPdHJpbV9wcm9wb3J0aW9ulEc/uZmZmZmZmnUu
</properties>
		<properties node_id="8" format="pickle">gASVgwEAAAAAAAB9lCiMGGF2ZXJhZ2Vfb3Zlcl90aW1lX3dpbmRvd5SJjARheGlzlIwEdGltZZSM
B2RldHJlbmSUjAhjb25zdGFudJSMCGZmdF9zaXpllIwNKHVzZSBkZWZhdWx0KZSMCG1ldGFkYXRh
lH2UjAhvbmVzaWRlZJSIjA9vdmVybGFwX3NhbXBsZXOUaAeME3NhdmVkV2lkZ2V0R2VvbWV0cnmU
jAlQeVF0Ni5zaXCUjA5fdW5waWNrbGVfdHlwZZSTlIwMUHlRdDYuUXRDb3JllIwKUUJ5dGVBcnJh
eZRDQgHZ0MsAAwAAAAACCgAAADIAAAOBAAAC7wAAAgoAAABOAAADgQAAAu8AAAAAAAAAAAWgAAAC
CgAAAE4AAAOBAAAC75SFlIeUUpSMB3NjYWxpbmeUjAdkZW5zaXR5lIwPc2VnbWVudF9zYW1wbGVz
lGgHjA5zZXRfYnJlYWtwb2ludJSJjAR1bml0lIwHc2FtcGxlc5SMBndpbmRvd5SMBGhhbm6UdS4=
</properties>
		<properties node_id="9" format="pickle">gASVKgMAAAAAAAB9lCiMDWFsd2F5c19vbl90b3CUiYwUYW5ub3RhdGlvbl9mb250X3NpemWUR0Am
AAAAAAAAjAthbnRpYWxpYXNlZJSIjBBhdXRvX2xpbmVfY29sb3JzlIiMCWF1dG9zY2FsZZSJjBBi
YWNrZ3JvdW5kX2NvbG9ylIwHIzMwMzAzMJSMCGNvbG9ybWFwlIwMZ2lzdF9yYWluYm93lIwQZGVj
b3JhdGlvbl9jb2xvcpSMByNCMEIwQjCUjAlmb250X3NpemWUR0AmAAAAAAAAjAxpbml0aWFsX2Rp
bXOUXZQoSzJLMk3oA00gA2WMDmxhYmVsX3JvdGF0aW9ulIwKaG9yaXpvbnRhbJSMC2xlZnRfb2Zm
c2V0lEsAjApsaW5lX2NvbG9ylIwFd2hpdGWUjApsaW5lX3dpZHRolEc/9AAAAAAAAIwMbWF4X2No
YW5uZWxzlEsjjAhtZXRhZGF0YZR9lIwVb25lX292ZXJfZl9jb3JyZWN0aW9ulImMC3Bsb3RfbWlu
bWF4lImME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjAlQeVF0Ni5zaXCUjA5fdW5waWNrbGVfdHlwZZST
lIwMUHlRdDYuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAAAAACEQAAADgAAAN4AAAC6QAA
AhEAAABUAAADeAAAAukAAAAAAAAAAAWgAAACEQAAAFQAAAN4AAAC6ZSFlIeUUpSMBXNjYWxllIwN
KHVzZSBkZWZhdWx0KZSMDnNldF9icmVha3BvaW50lImMDHNob3dfdG9vbGJhcpSJjAdzdGFja2Vk
lImMBnN0cmVhbZRoJYwLc3RyZWFtX25hbWWUaCWMDHRpZ2h0X2xheW91dJSIjAV0aXRsZZSMCFNw
ZWN0cnVtlIwVdHJhY2tfd2luZG93X3Bvc2l0aW9ulImMBHVuaXSUjAJkQpSMB3ZlcmJvc2WUiYwH
eF9sYWJlbJRoJYwHeF9yYW5nZZRoJYwHeV9sYWJlbJRoJYwHeV9yYW5nZZRdlChKhP7//0tkZYwK
emVyb19jb2xvcpSMByM2MDYwNjCUdS4=
</properties>
		<properties node_id="10" format="literal">{'average_over_time_window': False, 'axis': 'time', 'detrend': 'constant', 'fft_size': '(use default)', 'metadata': {}, 'onesided': True, 'overlap_samples': '(use default)', 'savedWidgetGeometry': None, 'scaling': 'density', 'segment_samples': '(use default)', 'set_breakpoint': False, 'unit': 'samples', 'window': 'hann'}</properties>
		<properties node_id="11" format="pickle">gASVKgMAAAAAAAB9lCiMDWFsd2F5c19vbl90b3CUiYwUYW5ub3RhdGlvbl9mb250X3NpemWUR0Am
AAAAAAAAjAthbnRpYWxpYXNlZJSIjBBhdXRvX2xpbmVfY29sb3JzlIiMCWF1dG9zY2FsZZSJjBBi
YWNrZ3JvdW5kX2NvbG9ylIwHIzMwMzAzMJSMCGNvbG9ybWFwlIwMZ2lzdF9yYWluYm93lIwQZGVj
b3JhdGlvbl9jb2xvcpSMByNCMEIwQjCUjAlmb250X3NpemWUR0AmAAAAAAAAjAxpbml0aWFsX2Rp
bXOUXZQoSzJLMk3oA00gA2WMDmxhYmVsX3JvdGF0aW9ulIwKaG9yaXpvbnRhbJSMC2xlZnRfb2Zm
c2V0lEsAjApsaW5lX2NvbG9ylIwFd2hpdGWUjApsaW5lX3dpZHRolEc/9AAAAAAAAIwMbWF4X2No
YW5uZWxzlEsjjAhtZXRhZGF0YZR9lIwVb25lX292ZXJfZl9jb3JyZWN0aW9ulImMC3Bsb3RfbWlu
bWF4lImME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjAlQeVF0Ni5zaXCUjA5fdW5waWNrbGVfdHlwZZST
lIwMUHlRdDYuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsAAwAAAAACEgAAADkAAAN5AAAC6gAA
AhIAAABVAAADeQAAAuoAAAAAAAAAAAWgAAACEgAAAFUAAAN5AAAC6pSFlIeUUpSMBXNjYWxllIwN
KHVzZSBkZWZhdWx0KZSMDnNldF9icmVha3BvaW50lImMDHNob3dfdG9vbGJhcpSJjAdzdGFja2Vk
lImMBnN0cmVhbZRoJYwLc3RyZWFtX25hbWWUaCWMDHRpZ2h0X2xheW91dJSIjAV0aXRsZZSMCFNw
ZWN0cnVtlIwVdHJhY2tfd2luZG93X3Bvc2l0aW9ulImMBHVuaXSUjAJkQpSMB3ZlcmJvc2WUiYwH
eF9sYWJlbJRoJYwHeF9yYW5nZZRoJYwHeV9sYWJlbJRoJYwHeV9yYW5nZZRdlChKnP///0tkZYwK
emVyb19jb2xvcpSMByM2MDYwNjCUdS4=
</properties>
		<properties node_id="12" format="pickle">gASVdQEAAAAAAAB9lCiMDWNsb3VkX2FjY291bnSUjA0odXNlIGRlZmF1bHQplIwMY2xvdWRfYnVj
a2V0lGgCjBFjbG91ZF9jcmVkZW50aWFsc5RoAowKY2xvdWRfaG9zdJSMB0RlZmF1bHSUjAhmaWxl
bmFtZZSMLi9Vc2Vycy9jeWMvRGVza3RvcC9ISVBfZmluYWwvc3ViLTEyX2V2ZW50cy5jc3aUjAht
ZXRhZGF0YZR9lIwLb3V0cHV0X3Jvb3SUaAKME3NhdmVkV2lkZ2V0R2VvbWV0cnmUjAlQeVF0Ni5z
aXCUjA5fdW5waWNrbGVfdHlwZZSTlIwMUHlRdDYuUXRDb3JllIwKUUJ5dGVBcnJheZRDQgHZ0MsA
AwAAAAACEgAAAKIAAAN5AAACfwAAAhIAAAC+AAADeQAAAn8AAAAAAAAAAAWgAAACEgAAAL4AAAN5
AAACf5SFlIeUUpSMDnNldF9icmVha3BvaW50lImMBnN0cmVhbZRoAnUu
</properties>
	</node_properties>
	<patch>{"description": {"description": "", "license": "", "name": "Final project", "status": "(unspecified)", "url": "", "version": "0.0.0"}, "edges": [["node2", "data", "node3", "data"], ["node2", "data", "node11", "data"], ["node3", "data", "node4", "data"], ["node3", "data", "node9", "data"], ["node6", "data", "node2", "data"], ["node6", "data", "node13", "data"], ["node7", "data", "node8", "data"], ["node8", "data", "node5", "data"], ["node1", "data", "node6", "data"], ["node4", "data", "node7", "data"], ["node9", "data", "node10", "data"], ["node11", "data", "node12", "data"]], "nodes": {"node1": {"class": "ImportSET", "module": "neuropype.nodes.file_system.ImportSET", "params": {"cloud_account": {"customized": false, "type": "StringPort", "value": ""}, "cloud_bucket": {"customized": false, "type": "StringPort", "value": ""}, "cloud_credentials": {"customized": false, "type": "StringPort", "value": ""}, "cloud_host": {"customized": false, "type": "EnumPort", "value": "Default"}, "filename": {"customized": true, "type": "StringPort", "value": "/Users/cyc/Desktop/HIP_final/sub-12_task-oddball_eeg_final.set"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "479b0c06-9a41-43f5-8e90-be9907acbe2c"}, "node10": {"class": "SpectrumPlot", "module": "neuropype.nodes.visualization.SpectrumPlot", "params": {"always_on_top": {"customized": false, "type": "BoolPort", "value": false}, "annotation_font_size": {"customized": false, "type": "FloatPort", "value": 11.0}, "antialiased": {"customized": false, "type": "BoolPort", "value": true}, "auto_line_colors": {"customized": false, "type": "BoolPort", "value": true}, "autoscale": {"customized": false, "type": "BoolPort", "value": false}, "background_color": {"customized": false, "type": "StringPort", "value": "#303030"}, "colormap": {"customized": false, "type": "EnumPort", "value": "gist_rainbow"}, "decoration_color": {"customized": false, "type": "StringPort", "value": "#B0B0B0"}, "font_size": {"customized": false, "type": "FloatPort", "value": 11.0}, "initial_dims": {"customized": false, "type": "ListPort", "value": [50, 50, 1000, 800]}, "label_rotation": {"customized": false, "type": "EnumPort", "value": "horizontal"}, "left_offset": {"customized": false, "type": "IntPort", "value": 0}, "line_color": {"customized": false, "type": "StringPort", "value": "white"}, "line_width": {"customized": false, "type": "FloatPort", "value": 1.25}, "max_channels": {"customized": true, "type": "IntPort", "value": 35}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "one_over_f_correction": {"customized": false, "type": "BoolPort", "value": false}, "plot_minmax": {"customized": false, "type": "BoolPort", "value": false}, "scale": {"customized": false, "type": "FloatPort", "value": null}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "show_toolbar": {"customized": false, "type": "BoolPort", "value": false}, "stacked": {"customized": false, "type": "BoolPort", "value": false}, "stream": {"customized": false, "type": "StringPort", "value": null}, "stream_name": {"customized": false, "type": "AliasPort", "value": null}, "tight_layout": {"customized": false, "type": "BoolPort", "value": true}, "title": {"customized": true, "type": "StringPort", "value": "Spectrum"}, "track_window_position": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": true, "type": "EnumPort", "value": "dB"}, "verbose": {"customized": false, "type": "BoolPort", "value": false}, "x_label": {"customized": false, "type": "StringPort", "value": ""}, "x_range": {"customized": true, "type": "ListPort", "value": null}, "y_label": {"customized": false, "type": "StringPort", "value": ""}, "y_range": {"customized": true, "type": "ListPort", "value": [-380, 100]}, "zero_color": {"customized": false, "type": "StringPort", "value": "#606060"}}, "uuid": "169d02f0-e2ba-44cd-b301-537309be4bdd"}, "node11": {"class": "WelchSpectrum", "module": "neuropype.nodes.spectral.WelchSpectrum", "params": {"average_over_time_window": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": false, "type": "ComboPort", "value": "time"}, "detrend": {"customized": false, "type": "EnumPort", "value": "constant"}, "fft_size": {"customized": false, "type": "IntPort", "value": null}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "onesided": {"customized": false, "type": "BoolPort", "value": true}, "overlap_samples": {"customized": false, "type": "FloatPort", "value": null}, "scaling": {"customized": false, "type": "EnumPort", "value": "density"}, "segment_samples": {"customized": false, "type": "FloatPort", "value": null}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": false, "type": "EnumPort", "value": "samples"}, "window": {"customized": false, "type": "EnumPort", "value": "hann"}}, "uuid": "dea0f0b6-dc1c-434c-b2a4-6b8a960f437c"}, "node12": {"class": "SpectrumPlot", "module": "neuropype.nodes.visualization.SpectrumPlot", "params": {"always_on_top": {"customized": false, "type": "BoolPort", "value": false}, "annotation_font_size": {"customized": false, "type": "FloatPort", "value": 11.0}, "antialiased": {"customized": false, "type": "BoolPort", "value": true}, "auto_line_colors": {"customized": false, "type": "BoolPort", "value": true}, "autoscale": {"customized": false, "type": "BoolPort", "value": false}, "background_color": {"customized": false, "type": "StringPort", "value": "#303030"}, "colormap": {"customized": false, "type": "EnumPort", "value": "gist_rainbow"}, "decoration_color": {"customized": false, "type": "StringPort", "value": "#B0B0B0"}, "font_size": {"customized": false, "type": "FloatPort", "value": 11.0}, "initial_dims": {"customized": false, "type": "ListPort", "value": [50, 50, 1000, 800]}, "label_rotation": {"customized": false, "type": "EnumPort", "value": "horizontal"}, "left_offset": {"customized": false, "type": "IntPort", "value": 0}, "line_color": {"customized": false, "type": "StringPort", "value": "white"}, "line_width": {"customized": false, "type": "FloatPort", "value": 1.25}, "max_channels": {"customized": true, "type": "IntPort", "value": 35}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "one_over_f_correction": {"customized": false, "type": "BoolPort", "value": false}, "plot_minmax": {"customized": false, "type": "BoolPort", "value": false}, "scale": {"customized": false, "type": "FloatPort", "value": null}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "show_toolbar": {"customized": false, "type": "BoolPort", "value": false}, "stacked": {"customized": false, "type": "BoolPort", "value": false}, "stream": {"customized": false, "type": "StringPort", "value": null}, "stream_name": {"customized": false, "type": "AliasPort", "value": null}, "tight_layout": {"customized": false, "type": "BoolPort", "value": true}, "title": {"customized": true, "type": "StringPort", "value": "Spectrum"}, "track_window_position": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": true, "type": "EnumPort", "value": "dB"}, "verbose": {"customized": false, "type": "BoolPort", "value": false}, "x_label": {"customized": false, "type": "StringPort", "value": ""}, "x_range": {"customized": true, "type": "ListPort", "value": null}, "y_label": {"customized": false, "type": "StringPort", "value": ""}, "y_range": {"customized": true, "type": "ListPort", "value": [-100, 100]}, "zero_color": {"customized": false, "type": "StringPort", "value": "#606060"}}, "uuid": "e932a08a-f6aa-483e-90b5-4d6f9977a046"}, "node13": {"class": "ExportMarkers", "module": "neuropype.nodes.markers.ExportMarkers", "params": {"cloud_account": {"customized": false, "type": "StringPort", "value": ""}, "cloud_bucket": {"customized": false, "type": "StringPort", "value": ""}, "cloud_credentials": {"customized": false, "type": "StringPort", "value": ""}, "cloud_host": {"customized": false, "type": "EnumPort", "value": "Default"}, "filename": {"customized": true, "type": "StringPort", "value": "/Users/cyc/Desktop/HIP_final/sub-12_events.csv"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "output_root": {"customized": false, "type": "StringPort", "value": ""}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "stream": {"customized": false, "type": "StringPort", "value": null}}, "uuid": "5eeda6c5-f85c-4a90-8fb9-4a8a11755ccc"}, "node2": {"class": "Rereferencing", "module": "neuropype.nodes.signal_processing.Rereferencing", "params": {"axis": {"customized": false, "type": "ComboPort", "value": "space"}, "cut_prop": {"customized": false, "type": "FloatPort", "value": 0.1}, "estimator": {"customized": false, "type": "EnumPort", "value": "mean"}, "ignore_nans": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "reference_range": {"customized": false, "type": "Port", "value": ":"}, "reference_unit": {"customized": false, "type": "EnumPort", "value": "auto"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "use_separate_reference": {"customized": false, "type": "BoolPort", "value": false}, "verbose": {"customized": false, "type": "BoolPort", "value": true}}, "uuid": "aaf9be96-880d-4df7-b4e9-41026d1f1770"}, "node3": {"class": "IIRFilter", "module": "neuropype.nodes.signal_processing.IIRFilter", "params": {"axis": {"customized": false, "type": "ComboPort", "value": "time"}, "design": {"customized": false, "type": "EnumPort", "value": "butter"}, "frequencies": {"customized": false, "type": "ListPort", "value": [0.1, 0.5, 45, 50]}, "ignore_nans": {"customized": false, "type": "BoolPort", "value": false}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "mode": {"customized": false, "type": "EnumPort", "value": "bandpass"}, "offline_filtfilt": {"customized": false, "type": "BoolPort", "value": false}, "order": {"customized": false, "type": "IntPort", "value": null}, "pass_loss": {"customized": true, "type": "FloatPort", "value": 0.5}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "stop_atten": {"customized": true, "type": "FloatPort", "value": 45.0}}, "uuid": "02bf5909-c2b3-463c-ba4b-2f52a0e3a2bb"}, "node4": {"class": "ArtifactRemoval", "module": "neuropype.nodes.neural.ArtifactRemoval", "params": {"a": {"customized": false, "type": "Port", "value": null}, "b": {"customized": false, "type": "Port", "value": null}, "block_size": {"customized": false, "type": "IntPort", "value": null}, "calib_seconds": {"customized": false, "type": "IntPort", "value": 45}, "cutoff": {"customized": false, "type": "FloatPort", "value": 7.5}, "emit_calib_data": {"customized": false, "type": "BoolPort", "value": true}, "init_on": {"customized": false, "type": "ListPort", "value": []}, "lookahead": {"customized": false, "type": "Port", "value": null}, "max_bad_channels": {"customized": false, "type": "FloatPort", "value": 0.2}, "max_dims": {"customized": false, "type": "FloatPort", "value": 0.0}, "max_dropout_fraction": {"customized": false, "type": "FloatPort", "value": 0.1}, "max_mem": {"customized": false, "type": "Port", "value": 256}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "min_clean_fraction": {"customized": false, "type": "FloatPort", "value": 0.25}, "min_required_channels": {"customized": false, "type": "IntPort", "value": 2}, "preserve_band": {"customized": false, "type": "DictPort", "value": null}, "riemannian": {"customized": false, "type": "BoolPort", "value": false}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "stddev_cutoff": {"customized": false, "type": "IntPort", "value": 20}, "step_size": {"customized": false, "type": "FloatPort", "value": 0.2}, "use_clean_window": {"customized": false, "type": "BoolPort", "value": true}, "use_legacy": {"customized": false, "type": "BoolPort", "value": false}, "window_len_cleanwindow": {"customized": false, "type": "FloatPort", "value": 0.5}, "window_length": {"customized": false, "type": "FloatPort", "value": 0.5}, "window_overlap": {"customized": false, "type": "FloatPort", "value": 0.66}, "window_overlap_cleanwindow": {"customized": false, "type": "FloatPort", "value": 0.66}, "zscore_thresholds": {"customized": false, "type": "ListPort", "value": [-5, 7]}}, "uuid": "dcdc1ff9-2fb9-4735-b0b6-6dc419c3a78e"}, "node5": {"class": "TimeSeriesPlot", "module": "neuropype.nodes.visualization.TimeSeriesPlot", "params": {"absolute_time": {"customized": true, "type": "BoolPort", "value": true}, "always_on_top": {"customized": false, "type": "BoolPort", "value": false}, "annotation_font_size": {"customized": false, "type": "FloatPort", "value": 11.0}, "antialiased": {"customized": false, "type": "BoolPort", "value": true}, "auto_line_colors": {"customized": false, "type": "BoolPort", "value": true}, "autoscale": {"customized": false, "type": "BoolPort", "value": true}, "background_color": {"customized": false, "type": "StringPort", "value": "#303030"}, "colormap": {"customized": false, "type": "EnumPort", "value": "gist_rainbow"}, "decoration_color": {"customized": false, "type": "StringPort", "value": "#B0B0B0"}, "font_size": {"customized": false, "type": "FloatPort", "value": 11.0}, "initial_dims": {"customized": false, "type": "ListPort", "value": [50, 50, 1000, 800]}, "label_rotation": {"customized": false, "type": "EnumPort", "value": "horizontal"}, "left_offset": {"customized": false, "type": "IntPort", "value": 0}, "line_color": {"customized": false, "type": "StringPort", "value": "white"}, "line_width": {"customized": false, "type": "FloatPort", "value": 1.25}, "marker_color": {"customized": false, "type": "Port", "value": "darkorange"}, "max_channels": {"customized": true, "type": "IntPort", "value": 35}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "nans_as_zero": {"customized": false, "type": "BoolPort", "value": false}, "no_concatenate": {"customized": false, "type": "BoolPort", "value": false}, "override_srate": {"customized": false, "type": "FloatPort", "value": null}, "plot_markers": {"customized": false, "type": "BoolPort", "value": false}, "plot_minmax": {"customized": false, "type": "BoolPort", "value": false}, "scale": {"customized": false, "type": "FloatPort", "value": 1.0}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "show_toolbar": {"customized": false, "type": "BoolPort", "value": false}, "stream": {"customized": false, "type": "StringPort", "value": null}, "stream_name": {"customized": false, "type": "AliasPort", "value": null}, "tight_layout": {"customized": false, "type": "BoolPort", "value": true}, "time_range": {"customized": true, "type": "FloatPort", "value": 6.0}, "title": {"customized": true, "type": "StringPort", "value": "Time Series"}, "track_window_position": {"customized": false, "type": "BoolPort", "value": false}, "verbose": {"customized": false, "type": "BoolPort", "value": false}, "x_axis": {"customized": false, "type": "ComboPort", "value": "time"}, "x_label": {"customized": false, "type": "StringPort", "value": ""}, "y_axis": {"customized": false, "type": "ComboPort", "value": "space"}, "y_label": {"customized": false, "type": "StringPort", "value": ""}, "zero_color": {"customized": false, "type": "StringPort", "value": "#606060"}, "zeromean": {"customized": false, "type": "BoolPort", "value": true}}, "uuid": "19d82864-c14e-4b17-9df6-f83e3f3b0f24"}, "node6": {"class": "DejitterTimestamps", "module": "neuropype.nodes.utilities.DejitterTimestamps", "params": {"force_monotonic": {"customized": false, "type": "BoolPort", "value": true}, "forget_halftime": {"customized": false, "type": "FloatPort", "value": 90.0}, "max_updaterate": {"customized": true, "type": "IntPort", "value": 1000}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "warmup_samples": {"customized": false, "type": "IntPort", "value": -1}}, "uuid": "adafb869-5058-4379-a767-4c13b771f46a"}, "node7": {"class": "Segmentation", "module": "neuropype.nodes.formatting.Segmentation", "params": {"keep_marker_chunk": {"customized": false, "type": "BoolPort", "value": false}, "max_gap_length": {"customized": false, "type": "FloatPort", "value": 0.2}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "online_epoching": {"customized": false, "type": "EnumPort", "value": "marker-locked"}, "sample_offset": {"customized": false, "type": "IntPort", "value": 0}, "select_markers": {"customized": false, "type": "ListPort", "value": null}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "time_bounds": {"customized": true, "type": "ListPort", "value": [-3, 3]}, "verbose": {"customized": false, "type": "BoolPort", "value": false}}, "uuid": "2450586b-fd0f-40c7-943b-69f79adb647d"}, "node8": {"class": "Mean", "module": "neuropype.nodes.statistics.Mean", "params": {"axis": {"customized": false, "type": "ComboPort", "value": "instance"}, "axis_occurrence": {"customized": false, "type": "IntPort", "value": 0}, "backend": {"customized": false, "type": "EnumPort", "value": "keep"}, "force_feature_axis": {"customized": false, "type": "Port", "value": null}, "ignore_nans": {"customized": false, "type": "BoolPort", "value": false}, "keep_axis": {"customized": false, "type": "BoolPort", "value": true}, "kept_axis": {"customized": false, "type": "ComboPort", "value": "legacy"}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "precision": {"customized": false, "type": "EnumPort", "value": "keep"}, "recurse_lists": {"customized": false, "type": "BoolPort", "value": false}, "robust": {"customized": false, "type": "BoolPort", "value": false}, "robust_estimator_type": {"customized": false, "type": "EnumPort", "value": "median"}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "trim_proportion": {"customized": false, "type": "FloatPort", "value": 0.1}}, "uuid": "f5076463-574c-4088-8b33-8ce9bac3c7e0"}, "node9": {"class": "WelchSpectrum", "module": "neuropype.nodes.spectral.WelchSpectrum", "params": {"average_over_time_window": {"customized": false, "type": "BoolPort", "value": false}, "axis": {"customized": false, "type": "ComboPort", "value": "time"}, "detrend": {"customized": false, "type": "EnumPort", "value": "constant"}, "fft_size": {"customized": false, "type": "IntPort", "value": null}, "metadata": {"customized": false, "type": "DictPort", "value": {}}, "onesided": {"customized": false, "type": "BoolPort", "value": true}, "overlap_samples": {"customized": false, "type": "FloatPort", "value": null}, "scaling": {"customized": false, "type": "EnumPort", "value": "density"}, "segment_samples": {"customized": false, "type": "FloatPort", "value": null}, "set_breakpoint": {"customized": false, "type": "BoolPort", "value": false}, "unit": {"customized": false, "type": "EnumPort", "value": "samples"}, "window": {"customized": false, "type": "EnumPort", "value": "hann"}}, "uuid": "ada4d230-b48b-46b3-b7c5-52e86f065e63"}}, "version": 1.1}</patch>
</scheme>
