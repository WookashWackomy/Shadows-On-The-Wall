import React from "react";
import PropTypes from "prop-types";
import {
  InteractiveForceGraph,
  ForceGraphNode,
  ForceGraphLink
} from "react-vis-force";

const InitiativeGraph = ({ graphData }) => {
  const prepareNodes = graphData => {
    const nodes = Object.assign([], graphData.nodes);
    const root = Object.assign({}, graphData.root);
    nodes.push(root);

    return nodes.map(node => {
      return {
        pk: node.pk,
        metric: node.metric,
        label: node.pk
      };
    });
  };

  const prepareEdges = graphData => {
    return graphData.edges.map(edge => {
      return [edge.source, edge.end];
    });
  };

  const handleSelectNode = pk => {
    //show panel with details?
  };

  return (
    <div>
      <InteractiveForceGraph
        simulationOptions={{ height: 300, width: 300 }}
        labelAttr="label"
        onSelectNode={node => console.log(node)}
        highlightDependencies
      >
        {prepareNodes(graphData).map(node => {
          // TODO: size + color depends on the metric value!
          return (
            <ForceGraphNode
              onSelectNode={() => handleSelectNode(node.pk)}
              node={{ pk: node.pk, label: node.label, radius: node.metric }}
              fill="red"
            />
          );
        })}

        {prepareEdges(graphData).map(edge => {
          return <ForceGraphLink link={{ source: edge[0], target: edge[1] }} />;
        })}
      </InteractiveForceGraph>
    </div>
  );
};

InitiativeGraph.propTypes = {};

export default InitiativeGraph;
