# Transcription of provided textbook excerpts (sections 4.3, 4.4, 4.5)
# This file contains literal transcriptions of text and formulas as multi-line strings.

content = {
    '4.3_MEASURING': r'''

4.3 MEASURING

The act of carrying out an observation on a given physical system is called measuring. Just as a single observable represents a specific question posed to the system, measuring is the process consisting of asking a specific question and receiving a definite answer.

In classical physics, we implicitly assumed that
- the act of measuring would leave the system in whatever state it already was, at least in principle; and
- the result of a measurement on a well-defined state is predictable, i.e., if we know the state with absolute certainty, we can anticipate the value of the observable on that state.

Both these assumptions proved wrong, as research in the subatomic scale has repeatedly shown: systems do get perturbed and modified as a result of measuring them. Furthermore, only the probability of observing specific values can be calculated: measurement is inherently a nondeterministic process.

Let us briefly recapitulate what we know: an observable can only assume one of its eigenvalues as the result of an observation. So far though, nothing tells us how frequently we are going to see a specific eigenvalue, say, λ. Moreover, our framework does not tell us yet what happens to the state vector if λ is actually observed. We need an additional postulate to handle concrete measures:

Postulate 4.3.1
Let Ω be an observable and |ψ> be a state. If the result of measuring Ω is the eigenvalue λ, the state after measurement will always be an eigenvector corresponding to λ.

''',

    'Example_4.3.1': r'''

Example 4.3.1
Let us go back to Example 4.2.1: It is easy to check that the eigenvalues of Ω are λ1 = -√2 and λ2 = √2 and the corresponding normalized eigenvectors are |e1> = [-0.923i, -0.382]^T and |e2> = [-0.382i, 0.923]^T.
Now, let us suppose that after an observation of Ω on |ψ> = 1/2[1, 1]^T, the actual value observed is λ1. The system has "collapsed" from |ψ> to |e1>.

''',

    'Exercise_4.3.1': r'''

Exercise 4.3.1
Find all the possible states the system described in Exercise 4.2.2 can transition into after a measurement has been carried out.

''',

    'Probability_projection_note': r'''

What is the probability that a normalized start state |ψ> will transition to a specific eigenvector, say, |e>? We must go back to what we said in Section 4.1: the probability of the transition to the eigenvector is given by the square of the inner product of the two states: |<e|ψ>|^2. This expression has a simple meaning: it is the projection of |ψ> along |e>.

''',

    'Mean_value_and_distribution': r'''

We are ready for a new insight into the real meaning of <Ω>_ψ of the last section: first, let us recall that the normalized eigenvectors of Ω constitute an orthogonal basis of the state space. Therefore, we can express |ψ> as a linear combination in this basis:

|ψ> = c_0 |e_0> + c_1 |e_1> + ... + c_{n-1} |e_{n-1}.         (4.81)

Now, let us compute the mean:

<Ω>_ψ = <ψ|Ω|ψ> = |c_0|^2 λ_0 + |c_1|^2 λ_1 + ... + |c_{n-1}|^2 λ_{n-1}.   (4.82)

As we can now see, <Ω>_ψ is precisely the mean value of the probability distribution

(λ_0, p_0), (λ_1, p_1), ..., (λ_{n-1}, p_{n-1}),                          (4.83)

where each p_i is the square of the amplitude of the collapse into the corresponding eigenvector.

''',

    'Example_4.3.2': r'''

Example 4.3.2
Let us go back to Example 4.3.1 and calculate the probabilities that our state vector will fall into one of the two eigenvectors:
p1 = |<ψ|e1>|^2 = 0.5  and  p2 = |<ψ|e2>|^2 = 0.5.                     (4.84)

Now, let us compute the mean value of the distribution:
p1 × λ1 + p2 × λ2 = 0.00,                                            (4.85)

which is precisely the value we obtained by directly calculating <ψ|Ω|ψ>.

''',

    'Note_same_measurement_repeat': r'''

Note: As a result of the foregoing discussion, an important fact emerges. Suppose we ask a specific question (i.e., we choose an observable) and perform a measurement once. We get an answer, say, λ, and the system transitions to the corresponding eigenvector. Now, let us ask the same question immediately thereafter. What is going to happen? The system will give exactly the same answer, and stay where it is. All right, you may say. But, what about changing the question? The following example will clarify matters.

''',

    '4.4_DYNAMICS': r'''

4.4 Dynamics

Postulate 4.4.1
The evolution of a quantum system (that is not a measurement) is given by a unitary operator or transformation.

That is, if U is a unitary matrix that represents a unitary operator and |ψ(t)> represents a state of the system at time t, then

|ψ(t + 1)> = U |ψ(t)>                                                      (4.86)

will represent the system at time t + 1.

An important feature of unitary transformations is that they are closed under composition and inverse, i.e., the product of two arbitrary unitary matrices is unitary, and the inverse of a unitary transformation is also unitary. Finally, there is a multiplicative identity, namely, the identity operator itself (which is trivially unitary). In math jargon, one says that the set of unitary transformations constitutes a group of transformations with respect to composition.

''',

    'Exercise_4.4.1': r'''

Exercise 4.4.1
Verify that
U1 = [[0, 1],
      [1, 0]]
and
U2 = [[√2/2,  √2/2],
      [√2/2, -√2/2]]
are unitary matrices. Multiply them and verify that their product is also unitary.

''',

    'Dynamics_sequence': r'''

We are now going to see how dynamics is determined by unitary transformations: assume we have a rule, U, that associates with each instant of time

t0, t1, t2, ..., t_{n-1}                                                   (4.88)

a unitary matrix

{U[t0], U[t1], ..., U[t_{n-1}]}.                                           (4.89)

Let us start with an initial state vector |ψ>. We can apply U[t0] to |ψ>, then apply U[t1] to the result, and so forth. We will obtain a sequence of state vectors:

U[t0] |ψ>,                                                                 (4.90)
U[t1] U[t0] |ψ>,                                                           (4.91)
...                                                                       (4.92)
U[t_{n-1}] U[t_{n-2}] ... U[t0] |ψ>.                                       (4.93)

Such a sequence is called the orbit of |ψ> under the action of {U[t]} at the time clicks t0, t1, ..., t_{n-1}.
Observe that one can always go back, just like running a movie backward, simply by applying the inverses of U[t0], U[t1], ..., U[t_{n-1}] in reverse order: evolution of a quantum system is symmetric with respect to time.

''',

    'Exercise_4.4.2': r'''

Exercise 4.4.2
Go back to Example 3.3.2 (quantum billiard ball), keep the same initial state vector [1, 0, 0, 0]^T, but change the unitary map to:
[ [0,  1/√2, 1/√2, 0],
  [1/√2, 0,   0,   1/√2],
  [1/√2, 0,   0,  -1/√2],
  [0,  1/√2, -1/√2, 0] ]                                                           (4.95)
Determine the state of the system after three time steps. What is the chance of the quantum ball to be found at point 3?

''',

    'Schrodinger_equation': r'''

The reader may wonder how the sequence {U[t]} of unitary transformations is actually selected in real-life quantum mechanics. In other words, given a concrete quantum system, how is its dynamics determined? How does the system change? The answer lies in an equation known as the Schrödinger equation:

|ψ(t + δt)> - |ψ(t)>
---------------   = -i (2π / h) H |ψ(t)>.                                (4.96)
   δt

A complete discussion of this fundamental equation goes beyond the scope of this introductory chapter. However, without going into technical details, we can at least convey its spirit. Classical mechanics taught physicists that the global energy of an isolated system is preserved throughout its evolution. Energy is an observable, and therefore for a concrete quantum system it is possible to write down a Hermitian matrix representing it (this expression will of course vary from system to system). This observable is called the Hamiltonian of the system, indicated by H in Equation (4.96).

The Schrödinger equation states that the rate of variation of the state vector |ψ(t)> with respect to time at the instant t is equal (up to the scalar factor 2π / h) to |ψ(t)> multiplied by the operator -i * H. By solving the equation with some initial conditions one is able to determine the evolution of the system over time.

''',

    'Time_for_a_small_recap': r'''

Time for a small recap:
- Quantum dynamics is given by unitary transformations.
- Unitary transformations are invertible; thus, all closed system dynamics are reversible in time (as long as no measurement is involved).
- The concrete dynamics is given by the Schrödinger equation, which determines the evolution of a quantum system whenever its Hamiltonian is specified.

''',

    'Programming_Drill_4.4.1': r'''

Programming Drill 4.4.1
Add dynamics to your computer simulation of the particle on a grid: the user should input a number of time steps n, and a corresponding sequence of unitary matrices U_n of the appropriate size. The program will then compute the state vector after the entire sequence U_n has been applied.

''',

    '4.5_Assembling_Quantum_Systems_intro': r'''

4.5 Assembling Quantum Systems

Exercise 4.5.2
Write down the generic state vector for the system of two particles with spin. Generalize it to a system with n particles (this is important: it will be the physical realization for quantum registers!).

Example 4.5.2
Let us work on the simplest nontrivial two-particle system: each particle is allowed only two points. Consider the state
|ψ> = |x0> ⊗ |y0> + |x1> ⊗ |y1>.                                      (4.103)

In order to clarify what is left out, we might write this as
|ψ> = 1|x0> ⊗ |y0> + 0|x0> ⊗ |y1> + 0|x1> ⊗ |y0> + 1|x1> ⊗ |y1>.       (4.104)
Let us see if we can write |ψ> as the tensor product of two states coming from the two subsystems. Any vector representing the first particle on the line can be written as
c0 |x0> + c1 |x1>.                                                      (4.105)
Similarly, any vector representing the second particle on the line can be written as
c0' |y0> + c1' |y1>.                                                     (4.106)

Therefore, if |ψ> came from the tensor product of the two subsystems, we would have
(c0|x0> + c1|x1>) ⊗ (c0'|y0> + c1'|y1>) = c0 c0' |x0> ⊗ |y0> + c0 c1' |x0> ⊗ |y1> + c1 c0' |x1> ⊗ |y0> + c1 c1' |x1> ⊗ |y1>. (4.107)

For our |ψ> in Equation (4.104) this would imply that c0 c0' = c1 c1' = 1 and c0 c1' = c1 c0' = 0. However, these equations have no solution. We conclude that |ψ> cannot be rewritten as a tensor product.

''',

    'Entanglement_discussion': r'''

Let us go back to |ψ> and see what it physically means. What would happen if we measured the first particle? A quick calculation will show that the first particle has a 50–50 chance of being found at the position x0 or at x1. So, what if it is, in fact, found in position x0? Because the term |x0> ⊗ |y1> has a 0 coefficient, we know that there is no chance that the second particle will be found in position y1. We must then conclude that the second particle can only be found in position y0. Similarly, if the first particle is found in position x1, then the second particle must be in position y1. Notice that the situation is perfectly symmetric with respect to the two particles, i.e., it would be the same if we measured the second one first. The individual states of the two particles are intimately related to one another, or entangled. The amazing side of this story is that the xi's can be light years away from the yj's. Regardless of their actual distance in space, a measurement's outcome for one particle will always determine the measurement's outcome for the other one.

The state |ψ> is in sharp contrast to other states like
|ψ'> = 1|x0> ⊗ |y0> + 1|x0> ⊗ |y1> + 1|x1> ⊗ |y0> + 1|x1> ⊗ |y1>.   (4.108)
Here, finding the first particle at a particular position does not provide any clue as to where the second particle will be found (check it!).

States that can be broken into the tensor product of states from the constituent subsystems (like |ψ'>) are called separable states, whereas states that are unbreakable (like |ψ>) are referred to as entangled states.

''',

    'Exercise_4.5.3': r'''

Exercise 4.5.3
Assume the same scenario as in Example 4.5.2 and let

|φ> = |x0> ⊗ |y1> + |x1> ⊗ |y1>.

Is this state separable?

''',

    'Spin_entanglement_intro': r'''

A clear physical case of entanglement is in order. We must revert to spin. Just as there are laws of conservation of momentum, angular momentum, energy-mass, and other physical properties, so too there is a law of conservation of total spin of a quantum system. This means that in an isolated system the total amount of spin must stay the same. Let us fix a specific direction, say, the vertical one (z axis), and the corresponding spin basis, up and down. Consider the case of a quantum system, such as a composite particle, whose total spin is zero. This particle might split up at some point in time into two other particles that do have spin (Figure 4.8).

The spin states of the two particles will now be entangled. The law of conservation of spin stipulates that because we began with a system of total spin zero, the sum of the spins of the two particles must cancel each other out. This amounts to the fact that if we measure the spin of the left particle along the z axis and we find it in state |↑_L> (where the subscript is to describe which particle we are dealing with), then it must be that the spin of the particle on the right will be |↓_R>. Similarly, if the state of the left particle is |↓_L>, then the spin of the right particle must be |↑_R>.

''',

    'Spin_basis_and_entangled_state': r'''

We can describe this within our notation. In terms of vector spaces, the basis that describes the left particle is B_L = {|↑_L>, |↓_L>} and the basis that describes the right particle is B_R = {|↑_R>, |↓_R>}. The basis elements of the entire system are

{|↑_L ⊗ ↑_R>, |↑_L ⊗ ↓_R>, |↓_L ⊗ ↑_R>, |↓_L ⊗ ↓_R>}                          (4.110)

In such a vector space, our entangled particles can be described by

(|↑_L ⊗ ↓_R> + |↓_L ⊗ ↑_R>) / √2                                          (4.111)

similar to Equation (4.104). As we said before, the combinations |↓_L ⊗ ↓_R> and |↑_L ⊗ ↑_R> cannot occur because of the law of conservation of spin. When one measures the left particle and it collapses to the state |↑_L> then instantaneously the right particle will collapse to the state |↓_R>, even if the right particle is millions of light-years away.

''',

    'What_have_we_learned_4.5': r'''

What have we learned?
- We can use the tensor product to build complex quantum systems out of simpler ones.
- The new system cannot be analyzed simply in terms of states belonging to its subsystems. An entire set of new states has been created, which cannot be resolved into their constituents.

''',

    'Programming_Drill_4.5.1': r'''

Programming Drill 4.5.1
Expand the simulation of the last sections by letting the user choose the number of particles.

''',

    'User_request': r'''

User request summary:
- Transcribe all provided images/photos into Python (pure transcription; do not solve exercises).
- Include formulas and text as literal strings, preserving numbering (e.g., 4.81, 4.82, 4.96).
- Also include a note: "Desarrolle e incluya en el Github una discusión de los ejercicios 4.5.2 y 4.5.3" (user task).

''',

    'User_followup_task': r'''
Desarrolle e incluya en el Github una discusión de los ejercicios 4.5.2 y 4.5.3
''',

}

# User follow-up task (in Spanish): Desarrolle e incluya en el Github una discusión de los ejercicios 4.5.2 y 4.5.3
