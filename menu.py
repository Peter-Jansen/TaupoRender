import nuke
import os

nuke.pluginAddPath('./tools')
nuke.pluginAddPath('./icons')

toolbar = nuke.toolbar('Nodes') # The default nuke nodes toolbaron the left hand side of screen
taupo_toolbar = toolbar.addMenu('TaupoRender', icon = 'p.png') # add menu for TaupoRender

# TaupoRender

taupo_toolbar.addCommand('TaupoRender', 'nuke.createNode(\'TaupoRender.nk\')', icon = 'p.png')
taupo_toolbar.addCommand('TaupoParticlePreview', 'nuke.createNode(\'TaupoParticlePreview.nk\')', icon = 'p.png')
taupo_toolbar.addSeparator()
taupo_toolbar.addCommand('TaupoParticleCache', 'nuke.createNode(\'TaupoParticleCache.nk\')', icon = 'p.png')
taupo_toolbar.addCommand('TaupoCustomCache', 'nuke.createNode(\'TaupoCustomCache.nk\')', icon = 'p.png')
taupo_toolbar.addCommand('TaupoCombineCache', 'nuke.createNode(\'TaupoCombineCache.nk\')', icon = 'p.png')
taupo_toolbar.addCommand('TaupoTransformCache', 'nuke.createNode(\'TaupoTransformCache.nk\')', icon = 'p.png')
taupo_toolbar.addSeparator()
taupo_toolbar.addCommand('TaupoGenerateCube', 'nuke.createNode(\'TaupoGenerateCube.nk\')', icon = 'p.png')
taupo_toolbar.addSeparator()
taupo_toolbar.addCommand('TaupoAdjustColour', 'nuke.createNode(\'TaupoAdjustColour.nk\')', icon = 'p.png')
taupo_toolbar.addCommand('TaupoCull', 'nuke.createNode(\'TaupoCull.nk\')', icon = 'p.png')
