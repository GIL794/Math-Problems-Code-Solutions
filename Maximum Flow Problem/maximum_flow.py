"""
Maximum Flow Problem Solver
===========================

This implementation solves the Maximum Flow Problem using the Ford-Fulkerson algorithm
with BFS (Edmonds-Karp variant) for finding augmenting paths.

The Maximum Flow Problem: Given a flow network with source and sink nodes,
find the maximum amount of flow that can be sent from source to sink.

Applications:
- Network routing and bandwidth allocation
- Bipartite matching problems
- Image segmentation
- Supply chain optimisation
- Sports scheduling
"""

from collections import deque
from typing import Dict, List, Tuple, Optional


class FlowNetwork:
    """
    Represents a flow network as an adjacency list.
    Each edge has a capacity and can carry flow up to that capacity.
    """
    
    def __init__(self, num_vertices: int):
        """
        Initialise a flow network with num_vertices vertices.
        
        Args:
            num_vertices: Number of vertices in the network (0-indexed)
        """
        self.num_vertices = num_vertices
        # Adjacency list: graph[u] = [(v, capacity), ...]
        self.graph: Dict[int, List[Tuple[int, int]]] = {i: [] for i in range(num_vertices)}
        # Residual graph: residual[u][v] = residual capacity from u to v
        self.residual: Dict[int, Dict[int, int]] = {i: {} for i in range(num_vertices)}
    
    def add_edge(self, u: int, v: int, capacity: int):
        """
        Add a directed edge from u to v with given capacity.
        
        Args:
            u: Source vertex
            v: Destination vertex
            capacity: Maximum flow capacity of the edge
        """
        if capacity < 0:
            raise ValueError("Capacity must be non-negative")
        
        # Add edge to graph
        self.graph[u].append((v, capacity))
        
        # Initialise residual capacities
        # Forward edge: u -> v with capacity
        # Backward edge: v -> u with 0 (can be used for flow cancellation)
        if v not in self.residual[u]:
            self.residual[u][v] = 0
        if u not in self.residual[v]:
            self.residual[v][u] = 0
        
        self.residual[u][v] += capacity
    
    def bfs_augmenting_path(self, source: int, sink: int, parent: List[int]) -> bool:
        """
        BFS to find an augmenting path from source to sink.
        Uses Edmonds-Karp approach: always finds shortest augmenting path.
        
        Args:
            source: Source vertex
            sink: Sink vertex
            parent: Array to store the path (parent[v] = u means edge u->v is in path)
        
        Returns:
            True if augmenting path found, False otherwise
        """
        visited = [False] * self.num_vertices
        queue = deque([source])
        visited[source] = True
        parent[source] = -1
        
        while queue:
            u = queue.popleft()
            
            # Check all neighbours
            for v in self.residual[u]:
                if not visited[v] and self.residual[u][v] > 0:
                    visited[v] = True
                    parent[v] = u
                    queue.append(v)
                    
                    if v == sink:
                        return True
        
        return False
    
    def ford_fulkerson(self, source: int, sink: int) -> Tuple[int, Dict[Tuple[int, int], int]]:
        """
        Ford-Fulkerson algorithm with BFS (Edmonds-Karp) to find maximum flow.
        
        Algorithm:
        1. While there exists an augmenting path from source to sink:
           a. Find path using BFS
           b. Find minimum residual capacity along path (bottleneck)
           c. Update residual capacities (forward edges decrease, backward edges increase)
        2. Return maximum flow and flow distribution
        
        Time Complexity: O(V * E²) where V = vertices, E = edges
        Space Complexity: O(V + E)
        
        Args:
            source: Source vertex
            sink: Sink vertex
        
        Returns:
            Tuple of (maximum_flow, flow_distribution)
            flow_distribution: Dictionary mapping (u, v) -> flow_value
        """
        if source == sink:
            return 0, {}
        
        # Flow distribution: how much flow goes through each edge
        flow_distribution: Dict[Tuple[int, int], int] = {}
        
        # Initialise flow distribution
        for u in range(self.num_vertices):
            for v in self.graph[u]:
                flow_distribution[(u, v[0])] = 0
        
        max_flow = 0
        parent = [-1] * self.num_vertices
        
        # Find augmenting paths until none exist
        while self.bfs_augmenting_path(source, sink, parent):
            # Find bottleneck capacity along the path
            path_flow = float('inf')
            v = sink
            
            # Trace back from sink to source to find minimum capacity
            while v != source:
                u = parent[v]
                path_flow = min(path_flow, self.residual[u][v])
                v = u
            
            # Update residual capacities and flow
            v = sink
            while v != source:
                u = parent[v]
                # Decrease forward edge capacity (flow uses it)
                self.residual[u][v] -= path_flow
                # Increase backward edge capacity (allows flow cancellation)
                self.residual[v][u] += path_flow
                
                # Update flow distribution
                if (u, v) in flow_distribution:
                    flow_distribution[(u, v)] += path_flow
                else:
                    # Flow is going backward (cancellation)
                    flow_distribution[(v, u)] -= path_flow
                
                v = u
            
            max_flow += path_flow
        
        return max_flow, flow_distribution
    
    def get_min_cut(self, source: int) -> Tuple[List[int], List[int]]:
        """
        Find the minimum cut (source side and sink side) after running Ford-Fulkerson.
        Uses BFS to find all vertices reachable from source in residual graph.
        
        Max-Flow Min-Cut Theorem: Maximum flow equals minimum cut capacity.
        
        Args:
            source: Source vertex
        
        Returns:
            Tuple of (source_side_vertices, sink_side_vertices)
        """
        visited = [False] * self.num_vertices
        queue = deque([source])
        visited[source] = True
        
        while queue:
            u = queue.popleft()
            for v in self.residual[u]:
                if not visited[v] and self.residual[u][v] > 0:
                    visited[v] = True
                    queue.append(v)
        
        source_side = [i for i in range(self.num_vertices) if visited[i]]
        sink_side = [i for i in range(self.num_vertices) if not visited[i]]
        
        return source_side, sink_side


def create_example_network_1() -> FlowNetwork:
    """
    Create example network 1: Classic textbook example.
    
    Source (0) -> A (1) -> B (2) -> Sink (3)
           |              |
            -> C (4) ->
    """
    network = FlowNetwork(5)
    network.add_edge(0, 1, 10)  # Source -> A
    network.add_edge(0, 4, 10)  # Source -> C
    network.add_edge(1, 2, 4)   # A -> B
    network.add_edge(1, 4, 2)   # A -> C
    network.add_edge(4, 2, 9)   # C -> B
    network.add_edge(2, 3, 10)  # B -> Sink
    network.add_edge(4, 3, 10)  # C -> Sink
    return network


def create_example_network_2() -> FlowNetwork:
    """
    Create example network 2: More complex network.
    """
    network = FlowNetwork(6)
    network.add_edge(0, 1, 16)  # Source -> 1
    network.add_edge(0, 2, 13)  # Source -> 2
    network.add_edge(1, 2, 10)  # 1 -> 2
    network.add_edge(1, 3, 12)  # 1 -> 3
    network.add_edge(2, 1, 4)   # 2 -> 1 (backward edge)
    network.add_edge(2, 4, 14)  # 2 -> 4
    network.add_edge(3, 2, 9)   # 3 -> 2
    network.add_edge(3, 5, 20)  # 3 -> Sink
    network.add_edge(4, 3, 7)   # 4 -> 3
    network.add_edge(4, 5, 4)   # 4 -> Sink
    return network


def create_bipartite_matching_example() -> FlowNetwork:
    """
    Create a bipartite graph matching example.
    This demonstrates how maximum flow solves bipartite matching.
    
    Left side: Jobs (0, 1, 2)
    Right side: Workers (3, 4, 5)
    Source connects to all jobs, all workers connect to sink.
    """
    network = FlowNetwork(7)  # 0=source, 1-3=jobs, 4-6=workers, 7=sink
    source = 0
    sink = 6
    
    # Source to jobs (capacity 1: each job can be assigned once)
    network.add_edge(source, 1, 1)
    network.add_edge(source, 2, 1)
    network.add_edge(source, 3, 1)
    
    # Jobs to workers (who can do which job)
    network.add_edge(1, 4, 1)  # Job 1 -> Worker 1
    network.add_edge(1, 5, 1)  # Job 1 -> Worker 2
    network.add_edge(2, 4, 1)  # Job 2 -> Worker 1
    network.add_edge(2, 6, 1)  # Job 2 -> Worker 3
    network.add_edge(3, 5, 1)  # Job 3 -> Worker 2
    network.add_edge(3, 6, 1)  # Job 3 -> Worker 3
    
    # Workers to sink (capacity 1: each worker can do one job)
    network.add_edge(4, sink, 1)
    network.add_edge(5, sink, 1)
    network.add_edge(6, sink, 1)
    
    return network


def print_network_info(network: FlowNetwork, source: int, sink: int):
    """Print network structure and solve maximum flow problem."""
    print("=" * 70)
    print("MAXIMUM FLOW PROBLEM SOLVER")
    print("=" * 70)
    print(f"\nNetwork: {network.num_vertices} vertices")
    print(f"Source: {source}, Sink: {sink}")
    print("\nEdges (with capacities):")
    print("-" * 70)
    
    for u in range(network.num_vertices):
        for v, capacity in network.graph[u]:
            print(f"  {u} -> {v}: capacity = {capacity}")
    
    print("\n" + "=" * 70)
    print("Solving Maximum Flow Problem...")
    print("=" * 70)
    
    max_flow, flow_dist = network.ford_fulkerson(source, sink)
    
    print(f"\n[OK] Maximum Flow: {max_flow}")
    print("\nFlow Distribution:")
    print("-" * 70)
    
    # Show only edges with non-zero flow
    active_flows = [(edge, flow) for edge, flow in flow_dist.items() if flow > 0]
    if active_flows:
        for (u, v), flow in sorted(active_flows):
            # Find original capacity
            original_capacity = next((cap for vert, cap in network.graph[u] if vert == v), 0)
            print(f"  {u} -> {v}: {flow}/{original_capacity} (flow/capacity)")
    else:
        print("  No flow (source and sink may be disconnected)")
    
    # Find and display minimum cut
    source_side, sink_side = network.get_min_cut(source)
    print(f"\nMinimum Cut:")
    print("-" * 70)
    print(f"  Source side: {source_side}")
    print(f"  Sink side: {sink_side}")
    
    # Calculate cut capacity
    cut_capacity = 0
    print(f"\nEdges in minimum cut:")
    for u in source_side:
        for v, capacity in network.graph[u]:
            if v in sink_side:
                cut_capacity += capacity
                print(f"  {u} -> {v}: capacity = {capacity}")
    
    print(f"\n[OK] Minimum Cut Capacity: {cut_capacity}")
    print(f"[OK] Verification (Max-Flow Min-Cut Theorem): {max_flow} = {cut_capacity}")
    
    return max_flow, flow_dist


def main():
    """Main function demonstrating maximum flow algorithms."""
    
    print("\n" + "=" * 70)
    print("EXAMPLE 1: Simple Network")
    print("=" * 70)
    network1 = create_example_network_1()
    print_network_info(network1, source=0, sink=3)
    
    print("\n\n" + "=" * 70)
    print("EXAMPLE 2: Complex Network")
    print("=" * 70)
    network2 = create_example_network_2()
    print_network_info(network2, source=0, sink=5)
    
    print("\n\n" + "=" * 70)
    print("EXAMPLE 3: Bipartite Matching (Job Assignment)")
    print("=" * 70)
    print("Problem: Assign 3 jobs to 3 workers (each can do specific jobs)")
    print("Goal: Maximum number of job assignments")
    print("-" * 70)
    network3 = create_bipartite_matching_example()
    max_matching, flow_dist = network3.ford_fulkerson(0, 6)
    
    print(f"\n[OK] Maximum Matching: {max_matching} jobs can be assigned")
    print("\nAssignments:")
    print("-" * 70)
    
    # Extract actual assignments
    jobs = {1: "Job A", 2: "Job B", 3: "Job C"}
    workers = {4: "Worker 1", 5: "Worker 2", 6: "Worker 3"}
    
    assignments = []
    for (u, v), flow in flow_dist.items():
        if flow > 0 and u in jobs and v in workers:
            assignments.append((jobs[u], workers[v]))
    
    if assignments:
        for job, worker in assignments:
            print(f"  {job} -> {worker}")
    else:
        print("  No assignments possible")
    
    print("\n" + "=" * 70)
    print("MATHEMATICAL INSIGHTS")
    print("=" * 70)
    print("""
1. Max-Flow Min-Cut Theorem:
   The maximum flow equals the minimum cut capacity.
   This fundamental theorem connects flow optimisation to graph cuts.

2. Ford-Fulkerson Algorithm:
   - Finds augmenting paths and pushes flow through them
   - With BFS (Edmonds-Karp): O(V * E²) time complexity
   - Guarantees optimal solution

3. Residual Graph:
   - Forward edges: remaining capacity
   - Backward edges: allow flow cancellation (undo previous flow)
   - Key insight: flow can be "undone" to find better paths

4. Applications:
   - Network routing: maximise data throughput
   - Bipartite matching: assign resources optimally
   - Image segmentation: separate foreground/background
   - Supply chains: maximise product flow
   - Sports scheduling: assign teams to time slots
    """)
    
    print("=" * 70)


if __name__ == "__main__":
    main()

