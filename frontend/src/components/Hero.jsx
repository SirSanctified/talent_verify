import SignInModal from "./SignInModal";

export default function Hero() {
  return (
    <main className="hero h-[50vh] lg:h-[60vh] px-4 md:px-0 flex flex-col items-center justify-center gap-8">
      <h1 className="text-3xl text-white font-black text-center">Revolutionary Talent Verification</h1>
      <p className="max-w-[60ch] text-center text-white">
        Unlock the full potential of your workforce with Talent Verify Online. The future of employee verification is here, and it's faster, more reliable, and easier to use than ever.
      </p>
      <SignInModal title="Get Started" />
    </main>
  );
}